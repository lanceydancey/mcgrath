# CS496/596: Network Security

**Location**: FAB 10 (MW 14:00-15:50)

**Instructor**: D. Kevin McGrath

* PDX username: dmcgrath
* Office hours:
    * Location: FAB 120-15 and [Zoom](https://pdx.zoom.us/j/84716901228) (PW: PSUSecure)
    * Times:
        * TBD

**TA**: 

* PDX username: 
* Office hours:
    * Location: TBD
    * Times: TBD

**Recorded Lectures**: These will be made available via [MediaSpace](https://media.pdx.edu/channel/channelid/328503742). Login required.

**Zulip Org**: [Zulip](https://netsec.zulip.cs.pdx.edu/)


## Course Description

Introduction to the skills and tools necessary to investigate network security. Packet capture, fuzzing, protocol analysis. Introduction to firewalls and intrusion prevention/detection systems.

Prerequisites: CS 201.

## Communication

Please post all course-related questions through zulip (more info coming) so that the whole class may benefit from our conversation. Please contact me privately via university supplied email for matters of a personal nature or if you are uncomfortable posting where the whole class can see/comment. I strive to reply to course-related questions within 24 hours. I will strive to return your assignments and grades for course activities to you within five business days of the due date. No other communication channels are used in this course.

# Student Learning Outcomes

Upon successful completion of this course, students will be able to:

1. Select among packet capture strategies for specific situations
1. Analyze protocols to determine potential security weaknesses
1. Create protocol fuzzers to find potential vulnerabilities
1. Select appropriate defensive strategies based on goals

# Evaluation of Student Performance
This course uses a weighted average of assignments. All assignments will be graded out of 100 points, with the following weights towards the final grade:

+ Weekly write-ups: 30%
+ Final Exam: 40%
+ Homework Assignments: 30%
+ While attendance will not be explicitly graded, it is expected that you will be involved in the classes.

### Letter Grade

Letter grades will be assigned based on standard ranges with (optionally) +/- steps.

| Grade | Percent Range |
| ----- | ------------- |
| A     | 90-100        |
| B     | 80-90         |
| C     | 70-80         |
| D     | 60-70         |
| F     | <60           |

## Course Content

| Week   | Topic                                      | Learning Activities                |
| ------ | ------------------------------------------ | ---------------------------------- |
| 1      | Introduction, policy, legal aspects, audit | Module summary, explorations*      |
| 2      | Network Reconnaissance                     | Module summary, explorations*      |
| 3      | Capturing packets with tcpdump             | Module summary, explorations*, HW1 |
| 4      | Packet capture with wireshark              | explorations*, module summary      |
| 5      | Packet processing with scapy               | HW2, explorations*, module summary |
| 6      | Advanced scapy                             | HW3, explorations*, module summary |
| 7      | Protocol reversing                         | explorations*, module summary      |
| 8      | Protocol fuzzing                           | HW4, explorations*, module summary |
| 9      | Firewalls                                  | Explorations*, module summary      |
| 10     | IPS/IDS                                    | Explorations*, module summary      |
| Finals |                                            | Final paper                        |

*Explorations are ungraded learning activities that typically involve a hands-on activity related to the current topic. These include usages of tools, looking at packet captures, etc.

## Course Policies

### Late Work Policy

No late work will be accepted without prior discussion. I understand that life happens, but request for late hand-in must be submitted prior to the due date. Permission will be granted dependent upon reasons, current state of completion, etc.

### Incompletes
Incomplete (I) grades will be granted only in emergency cases (usually only for a death in the family, major illness or injury, or birth/adoption of a child), and if the student has turned in 90% of the points possible AT THE TIME OF REQUEST. In other words, if you have been keeping up, but a major life event occurs, let me know as soon as possible. If you are having any difficulty that might prevent you completing the coursework, please don’t wait until the end of the term; let me know right away.

## Academic or Student Support Services

### Accommodations

Accommodations for students with disabilities are determined and approved by Disability Resource Center (DRC). If you, as a student, believe you are eligible for accommodations but have not obtained approval please contact DRC immediately at 503-725-4150, drc@pdx.edu, or https://www.pdx.edu/disability-resource-center. DRC notifies students and faculty members of approved academic accommodations and coordinates implementation of those accommodations. If you have accommodations through DRC and wish to take the Midterm or Final Exam in the testing center, I strongly recommend that you schedule it before the end of week 1. If you are not registered with the DRC, you cannot register to take an exam in the testing center.

I want to make this class an open and welcoming environment for all. Your success is my goal.

### Religious Observance

Portland State University strives to respect all religious practices. If you have religious holidays that conflict with any of the requirements of this class, please see me immediately so that we can make alternative arrangements.

### Reach Out for Success

The PSU [Center for Student Health and Counseling (SHAC)](https://www.pdx.edu/health-counseling/) is staffed with folks who care and can help with a wide range of personal challenges. Here at PSU, there is never a need to tough things out alone.  

As a student you may experience a range of issues that can cause barriers to learning, such as strained relationships, increased anxiety, alcohol/drug problems, feeling down, difficulty concentrating and/or lack of motivation. These mental health concerns or stressful events may lead to diminished academic performance or reduce a student’s ability to participate in daily activities. PSU is committed to advancing the mental health and well-being of its students. If you or someone you know is feeling overwhelmed, depressed, and/or in need of support, services are available. You can learn more about the broad range of confidential mental health services available on campus via SHAC https://www.pdx.edu/health-counseling/.

SHAC also has resources for physical health, including flu shots. You can check out their COVID-19 resources page here: https://www.pdx.edu/health-counseling/covid-19-resources (including testing).

[Get Food Now](https://www.pdx.edu/student-access-center/food-assistance) Here at PSU, there is never a need to tough things out alone. Those who can, give, so those who need, have.

[Housing / financial crisis help](https://www.pdx.edu/dean-student-life/student-homelessness-and-economic-crisis) Here at PSU, there is never a need to tough things out alone. Emergency Housing, etc.

### Title IX

As an instructor, students frequently come to me for assistance in matters that are not related to the course material. Please be aware that PSU’s policies require instructors to report any instance of sexual harassment, sexual and relationship violence and/or other forms of prohibited discrimination to University Officials, who keep the information private. If you would rather share information about these experiences with a PSU staff member who does not have these reporting responsibilities and can keep the information confidential, please contact one of the following campus resources.

+ Confidential Advocates: 503.894.7982, or by [scheduling on-line](https://www.google.com/url?q=https://psuwrc.youcanbook.me/&sa=D&source=editors&ust=1648503453184575&usg=AOvVaw0RnqMNvCBNc--7kOcXteWW) (for matters regarding sexual harassment and sexual and relationship violence)
+ [Center for Student Health and Counseling (SHAC)](https://www.pdx.edu/health-counseling/): 1880 SW 6th Ave, 503.725.2800
+ [Student Legal Services](https://www.google.com/url?q=https://www.pdx.edu/student-legal-services/&sa=D&source=editors&ust=1648503453185428&usg=AOvVaw0Yfw3-vB8E1gxcjod2WfI6): 1825 SW Broadway, (SMSU) M343, 503.725.4556 

[PSU Sexual Misconduct Response website](https://www.google.com/url?q=https://www.pdx.edu/sexual-assault/&sa=D&source=editors&ust=1648503453186003&usg=AOvVaw0kjTNvErvB5aNsMon4XKsT) gives you comprehensive information about how to support and/or report an incident.

Please complete the required student module [Understanding Sexual Misconduct and Resources](https://www.google.com/url?q=https://www.pdx.edu/diversity/understanding-sexual-misconduct-and-resources-student-module&sa=D&source=editors&ust=1648503453186548&usg=AOvVaw1QAxgICH1QI4x82uY-d1R0) in Canvas, which provides information about PSU policy and resources.

You may also report sexual and relationship violence to law enforcement on campus with [Campus Public Safety Office (CPSO)](https://www.google.com/url?q=https://www.pdx.edu/campus-safety/&sa=D&source=editors&ust=1648503453187321&usg=AOvVaw3tlkVac2wvw2rNVcAONxzT)

Or you may file an [anonymous report](https://www.google.com/url?q=https://docs.google.com/a/pdx.edu/forms/d/e/1FAIpQLScGJ2EsjqRT9MBkEkQCAuaeLfvZBiRDfHztvIEzMyCqO3DVJg/viewform&sa=D&source=editors&ust=1648503453188378&usg=AOvVaw34vcWBUk49whsysC6vhKX9) with [Campus Public Safety Office](https://www.google.com/url?q=https://www.pdx.edu/campus-safety/make-report&sa=D&source=editors&ust=1648503453188903&usg=AOvVaw3Xmu_iRL_ohJkBE9_wdUkK) or a [Bias Incident report](https://www.google.com/url?q=https://web.imaging.pdx.edu/AppNet/UnityForm.aspx?key%3DUFKey&sa=D&source=editors&ust=1648503453189336&usg=AOvVaw39Py9CfwBcDBS09re3kuCn) with the [Bias Review Team (BRT)](https://www.google.com/url?q=https://www.pdx.edu/diversity/bias-review-team&sa=D&source=editors&ust=1648503453189761&usg=AOvVaw3W0x7iOkMKgmykW6T0ksdn). PSU does not typically investigate the reports that are made through these two avenues. These reports help PSU understand what students and employees are experiencing on and around campus and provide support where needed.