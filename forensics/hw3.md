# File Carving

Due Date: 2024-02-26 23:59:59

* auto-gen TOC:
{:toc}

## Introduction

In this lab, we'll be investigating a forensic image of thumb drive taken from a woman named Jenny Card, who was arrested in Chicago selling fraudulent gift cards from several retail stores. The SHA-256 hash of the image is: ba4a638911e1824c5a84ea4dfb870bcbcff36a6775eaf8108e48b2ceee0c7335. You should be able to find evidence linking her to the crime in the image. This will take a lot of careful sifting of data, but you got this!

Get the image via scp from `ada.cs.pdx.edu:/disk/scratch/forensics/fsf.dd.bz2`.

## Mount the image
You have been supplied with a forensic image of a thumb drive. As in the previous lab, we'll need to mount the forensic image. Use mmls to view the partitions and calculate the offset.

```sh
❯ sudo kpartx -av fsf.dd
```

Make note of the output of this command, as you'll need the loop device number. 

```sh
❯ mkdir ~/fsf
❯ sudo mount -t ntfs-3g -o ro,noexec /dev/mapper/loopXp2 ~/fsf
```

Replace X with the actual loop device number from above.

After you mount the drive you'll see that the partition contains nothing. The drive was formatted before the investigators imaged it. We'll need to use file carving in this investigation. Well, shoot. 

## Manual file carving

Let's first try to understand how file carving tools work by doing a little manual file carving. Across operating systems, magic numbers have been standardized to differentiate between file types. Let's find the magic number for JPEG files. xxd is a hex editor that should be installed. Use it to identify the first 2 bytes in the file and the last 2 bytes of cat.jpg. These are the header and footer found in every JPEG. Every instance of these values on the drive won't necessarily mean that you're looking at a JPEG, so you might want to take a look more closely at the JPEG header to see if there are other useful strings that JPEGs have in common. Write the hex code for the

* header:
* footer:

These magic number values should enable you to find the beginning and end of a JPEG without using the file system. Let's try to use this information to manually carve an image out of this lab's disk image. Find the start and end of the JPEG and use these to compute the size.


```sh
❯ xxd fsf.dd | grep header
❯ xxd -s <start in decimal> fsf.dd | grep footer
```
This will generate an enormous quantity of output. Ensure the offset you pick includes other parts of the JPEG header (usually something like JFIF).

* start:
* end:
* size:

### Hints

Remember to convert the start and end into decimal.
Don't forget that the hex editor gives the address of the first byte on the line.
Remember that you need to include the footer itself in the portion you're carving out. Make sure to adjust your offset size appropriately.

## Extracting the image

Now we'll use dd to lift the JPEG out of the disk image.

```sh
❯ dd if=fsf.dd of=image.jpg skip=start bs=1 count=size
```

You should now be able to open image.jpg with an image viewer.

* What do you see?
* How many colors are in the image?

## Automated file carving

The simple principle of the previous section is the method that automated file carving tools use to extract files from a disk image. These automated tools aren't perfect, however. Running them will produce both false positives and false negatives. They are also slow and require a large amount of disk space to run. You'll have to be smarter than the tools to get the information you want.

### foremost and scalpel
Foremost and scalpel are two common file carving tools. They completely ignore the file system, so you could potentially point them at a RAM dump or swap file. Here's an example of how to install and run foremost.


```sh
❯ sudo apt-get install foremost
❯ foremost -T -t jpg,gif,pdf -i fsf.dd
```

What images are returned? Can you find anything of interest to our investigation?

### photorec
phohotorec is a file carving tool that tries to discern some data about the file system (e.g. block size) to carve more effectively. This means it has some assumptions baked in about file systems, so it won't work with all images.

```sh
❯ sudo apt-get install testdisk
❯ photorec fsf.dd
```

Use the interactive menu to choose the image you'd like to carve. This should produce digital evidence in file formats you are familiar with from the previous lab. With the combined output of foremost and photorec, you should be able to conduct your investigation.

## Visualization

You should now have a collection of images and other files that you can use to conduct your investigation. You should be able to find evidence linking Jenny Card to the crime in the images. One way to look at the data is spatially: you can plot the GPS coordinates of each image (that has them) on a map.

Write a program that does the following:

* Given a directory of images, extract the GPS coordinates from the EXIF data of each image, taking care to handle images that don't have GPS data. Keep track of which image contains which coordinates.
* Plot the coordinates on some form of HTML map. You can use whatever mapping API you desire.
    * Python has folium, which makes plotting on a map fairly easy.
    * You can also use Google Maps or OpenStreetMap, as you desire.
    * I'm told this is doable in Rust, but YMMV.
* While I would recommend doing this in python, you can use whatever language you like, as long as you include any instructions necessary to run your code.
* Save the HTML generated map file to your gitlab repo.

## Report
Write a 1-2 page comprehensive forensic report of your findings with the following sections:

* Summary - a brief summary of the report.
* Purpose - explain the purpose of your investigation
* Methodology - describe the tools and methods you used to investigate the evidence
* Findings - clearly state the facts you uncovered from your investigation in an unbiased way
* Conclusions - summarize your findings and describe how they relate to the overall case

This report should be in `hw3/hw3.md` in your gitlab repo.