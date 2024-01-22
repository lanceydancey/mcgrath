# Digital Evidence

## Introduction

You've been hired by Booring Soft to investigate an employee named Kevin Tunes. Kevin's supervisor is fed up with him for not getting work done. His coworkers report that he browses websites all day and streams music. Both of these actions are explicitly against company policy. One coworker even alleges that Kevin has been traveling on the company money to conferences, but hasn't been attending the conferences.

The company authorized travel for Kevin to attend conferences on these dates:

* 2011
  * Mar 13-18 Memphis
  * Mar 21-25 New Orleans
  * Jul 14-20 Chicago
  * Oct 04-06 St. Louis
* 2012
  * Feb 20-21 Las Vegas
  * Jun 07-10 Nashville
  * Jul 12-15 Chicago
* 2013
  * Jan 23-25 Minnesota
  * Jul 16-20 Chicago
* 2014
  * Mar 19-21 Indianapolis

## Part 1: Creating a forensic image
The first task will be to create a forensic image of the drive. This is an exact bit-for-bit copy of all sectors of the drive. Additionally, we will create digital fingerprint of the drive using the SHA-256 hash algorithm. We will accomplish both of these tasks with a program called dc3dd, which is a specialized forensic imaging program developed at the DoD Cyber Crime Center.

First, snag the [`del.dd.bz2` image](https://web.mcecs.pdx.edu/~dmcgrath/del.dd.bz2). and decopmress it:

```sh
$ curl -LO https://web.mcecs.pdx.edu/~dmcgrath/del.dd.bz2
$ bzip2 -dc del.dd.bz2 > del.dd
```

Then, create a forensics image of the drive (which is really an image) using dc3dd. This will take some time.

```sh
$ sudo apt-get install dc3dd
$ dc3dd if=del.dd of=out.dd verb=on hash=sha256 hlog=out.hashlog log=log rec=off
```



## Part 2: Mounting a forensic image

Create the mount point using mkdir, then mount the image.

```sh
$ mkdir ~/out
$ sudo mount -t ntfs-3g -o loop,ro,noexec out.dd ~/out
```

What do the flags to mount do? Why are they important in this context?

## Part 3: Digital artifacts

### Digital photo artifacts

Digital photos are a common source of evidence. In particular, the metadata stored in the file can be very revealing. Let's start by looking in the pictures folder.

```sh
$ cd ~/out/Documents and Settings/Kevin Tunes/Pictures/
```

Let's view the first picture in a hex editor.

```sh
$ xxd 01.jpg | less
```

As you browse through the raw bytes of the image, you should see there is a wealth of meta-data stored inside the image. Let's download a tool specifically designed to parse JPEG metadata and look at this image.

```sh
$ sudo apt-get install exiftool
$ exiftool 01.jpg  
```

From this metadata, you should be able to determine exactly where and when this photo was taken, as well as the device used to take the photo.

Take a look at the others. Can you determine where and when these photos were taken? Compare these to the dates and locations of the conference travel authorized by the company. We will be creating a tool later to automate this process.

### Portable Document Format artifacts

As with images, PDFs contain useful metadata. There is a PDF in the Documents folder. exiftool can extract metadata from PDFs as well as images.

```sh
$ cd ~/out/Documents and Settings/Kevin Tunes/Documents/
$ exiftool 11291307605-327242879-ticket.pdf 
```

You should be able to determine when this PDF was created and by whom.

### OLE/OOXML artifacts

Microsoft Office documents also store useful metadata. Interestingly, the OOXML (docx) format is essentially just a glorified zip file. We'll use this fact to extract the XML formatted metadata.

```sh
$ mkdir ~/mfb
$ cp My Favorite Bands.docx ~/mfb/mfb.zip
$ cd ~/mfb
$ unzip mfb.zip 
```

You should be able to find out the creator of the document by viewing docProps/core.xml in your favorite text editor. If you prefer to view a nicely formatted version of the XML, you can use this command.

```sh
$ xmllint --format docProps/core.xml
```

Exploring this and other XML files, you should be able to determine who created this document and what software they used to create the document. In fact, you can even reconstruct the edit history of the document using the file word/document.xml

If you want to view metadata for older OLE files (.doc), you can use the wvWare tool, which can be installed and run as follows.

```sh
$ sudo apt install wv
$ wvSummary yourDocument.doc
```

### Web Browser artifacts

As you might guess, browsing the web generates a wealth of interesting artifacts. While different browsers store history using different methods, both Chrome and Firefox use SQLite databases. Though we will examine a Firefox profile, the general principles we use can be extrapolated to other browsers. First, we’ll copy the database and start up SQLite. Then we’ll look at the tables in the database and issue a few queries from the command line. Alternatively, you could use a tool like [DataGrip](https://www.jetbrains.com/datagrip/) to view the database.

```sh
cp -r ~/del/Users/Kevin Tunes/Application Data/Mozilla/Firefox/Profiles/obaosuzs.default ~/
cd obaosuzs.default
sqlite3 places.sqlite
```

We can view the tables in the database and issue queries from the SQLite interface. Let’s look at the contents of two interesting tables.

```sql
.tables
SELECT * FROM moz_places;
SELECT * FROM moz_historyvisits;
```

Since you might not have experience writing SQL queries, below is a query that joins these two tables to create a history of the websites visited in this browser profile.

```sql
SELECT datetime(moz_historyvisits.visit_date/1000000, 'unixepoch', 'localtime'), moz_places.url FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id;
```

With the right queries against this database, you can now determine which websites were visited and when they were visited. Other interesting databases are `cookies.sqlite` and `formhistory.sqlite`. Try writing a few queries against these databases to see what they contain.

## Report

A report format may be found here: http://www.testifyingtraining.com/the-ideal-expert-witness-report-format/Links to an external site..

Please read this short summary of how to write an effective expert witness report:

James J. Mangraviti, Steven Babitsky, and Nadine Nasser Donovan, “How to Draft a Powerful, Persuasive, and Understandable Expert Witness Report,” SEAK, Inc., 2014. [Online](http://www.testifyingtraining.com/wp-content/uploads/2014/07/How-to-Draft-a-Powerful-Expert-Witness-Report-6-30-2014.pdf)

Write a 1-2 page comprehensive forensic report of your findings with the following sections:

* Summary - a brief summary of the report
* Purpose - explain the purpose of your investigation
* Methodology - describe the tools and methods you used to investigate the evidence
* Findings - clearly state the facts you uncovered from your investigation in an unbiased way
* Conclusions - summarize your findings and describe how they relate to the overall case