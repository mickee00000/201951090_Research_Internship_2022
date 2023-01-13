<!-- Output copied to clipboard! -->

<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 38

Conversion time: 7.457 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Fri Jan 13 2023 02:10:02 GMT-0800 (PST)
* Source doc: Copy of Summer Research Intership 2022
* This is a partial selection. Check to make sure intra-doc links work.
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 38.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>
<a href="#gdcalert10">alert10</a>
<a href="#gdcalert11">alert11</a>
<a href="#gdcalert12">alert12</a>
<a href="#gdcalert13">alert13</a>
<a href="#gdcalert14">alert14</a>
<a href="#gdcalert15">alert15</a>
<a href="#gdcalert16">alert16</a>
<a href="#gdcalert17">alert17</a>
<a href="#gdcalert18">alert18</a>
<a href="#gdcalert19">alert19</a>
<a href="#gdcalert20">alert20</a>
<a href="#gdcalert21">alert21</a>
<a href="#gdcalert22">alert22</a>
<a href="#gdcalert23">alert23</a>
<a href="#gdcalert24">alert24</a>
<a href="#gdcalert25">alert25</a>
<a href="#gdcalert26">alert26</a>
<a href="#gdcalert27">alert27</a>
<a href="#gdcalert28">alert28</a>
<a href="#gdcalert29">alert29</a>
<a href="#gdcalert30">alert30</a>
<a href="#gdcalert31">alert31</a>
<a href="#gdcalert32">alert32</a>
<a href="#gdcalert33">alert33</a>
<a href="#gdcalert34">alert34</a>
<a href="#gdcalert35">alert35</a>
<a href="#gdcalert36">alert36</a>
<a href="#gdcalert37">alert37</a>
<a href="#gdcalert38">alert38</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>


**     Indian Institute of Information Technology, Vadodara **

**                             (Gandhinagar Campus)**

**Summer Research Internship - 2022**

**<span style="text-decoration:underline;">Extraction of melodies with pitch classes From images of HCM compositions in Bhatkhande notation</span>**

under the mentorship of

**Dr.Pratik Shah**

Submitted by

**Manjot Singh (201951090)**

**Abstract - Conversion of Music Notes from images of Bhatkhande Notation System into MIDI file(audio file) involving Images Processing using OpenCV, Deep convolutional neural network modeling using Tensorflow and Keras and extracting those notes to be converted into a playable audio file using music21 toolkit for computer-aided musicology. The source code and other involved files for this project can be found [here](https://github.com/mickee00000/201951090_Research_Internship_2022).**



1. 
 Introduction 
The Indian Classical Music holds a very high place in our Indian culture, to the point that it is synonymous to Indian festivals, religious customs, marriages, exotic cuisine and Traditional Clothing. Doesn’t matter who you are or what part of India you belong to, the minute you hear Indian music, the nostalgia and the amusement kicks in. Even if you are not from India, it would still create a sense of elegance and simplistic pleasures. 

But despite its legendary status in the music culture, it seems that it is not being practiced heavily by the masses. Part of the reason is that it is less accessible and not being able to be visualized from reading about it in books and online articles. We are living in the age of social media and Short Clips platforms which tend to cause low attention span. “TikTok use disorder (TTUD) is positively linked to memory loss, and it is also positively linked to depression, anxiety, and stress. Depression, anxiety, and stress are positively linked to memory loss. Furthermore, depression, anxiety, and stress have a mediating effect between TTUD and memory loss.” [1] 

This project tries to bridge that gap between written medium and being able to hear and picture the beauty of the melodies. To be able to just convert your favorite melodies instantly from  unexciting texts in your old books to audio files in your phone or laptop almost seems like a dream come true for a music enthusiast. 



2. 
Problem Statement
Now that we understand the importance of the project, we need to understand and break down what are the necessary steps we need to take to solve this problem.



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.jpg "image_tooltip")



## <span style="text-decoration:underline;">Task</span>: From images of HCM compositions in Bhatkhande notation, extract the melodies with pitch classes.


## So, initially this image needs to be converted into a supported audio file. 



3. 
Proposed Solution
A lot of approaches had to be considered for this project. The final approach ended up being diving this task into 3 parts:



* NOTATION RECOGNITION AND PROCESSING
* NOTATION CLASSIFICATION
* AUDIO EXTRACTION

Or in simpler terms, this is divided as:



* What to read in this image?
* What is the meaning of the part that I just read in the image?
* What sound to produce in response to what I just read.

**<span style="text-decoration:underline;">PART A</span> - **NOTATION RECOGNITION AND PROCESSING

For this, OpenCV is used to convert the notation image to a data array of the image. First comes Preprocessing of the image in which all the extra noise on the image is removed, like the color of the paper, different shades of color etc, so  that it would not interfere with the detection[3]. After this we end up with a binary version of the image where only two colors exist, Black (0,0,0) and White(255,255,255).



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.jpg "image_tooltip")


After that, contours(outline along the boundary) of the image are detected, extracted and drawn onto another blank image.



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.jpg "image_tooltip")


Using these contours, Bounding Rectangles are drawn on the co-ordinates of these contours and saved on another blank image.



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.jpg "image_tooltip")


After getting all the bounding rectangles of all the contours out of the image, selective filtering of the contours is done for classification and thus removing the unnecessary clutter like vertical lines[2], heading, numberings etc. 

We get x, y, h, w from contours as properties. For filtering, 4 conditions were set:



* **h / w &lt; 3**, i.e. _Height / Width should be less than 3_ (This removes all the tall lines which have a lot more height than width).
* **w / h &lt; 2**, i,e. _Width / Height should be less than 2_ (This removes all the horizontal lines and heading  which have a lot more width than height).
* **h  > 20,  **i.e. _h should be greater than 20px _(This removes smaller elements such as numbers or dots)
* **w> 18, **i.e. _w should be greater that 18px _(This removes marks and numberings)



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.jpg "image_tooltip")


And Voila, we ended up with the desired elements needed for the classification. These elements are cut out of the original binary images in order for the classification.[5]



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.jpg "image_tooltip")


After this, we need to pass these bounded cutout elements in an array for further classification in the Deep CNN Model.



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.jpg "image_tooltip")


<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image8.jpg "image_tooltip")


<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image9.jpg "image_tooltip")


<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image10.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image10.jpg "image_tooltip")


<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image11.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image11.jpg "image_tooltip")


<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image12.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image12.jpg "image_tooltip")


<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image13.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image13.jpg "image_tooltip")


<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image14.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image14.jpg "image_tooltip")


<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image15.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image15.jpg "image_tooltip")


<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image16.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image16.jpg "image_tooltip")


**<span style="text-decoration:underline;">PART B</span> - **NOTATION CLASSIFICATION

A lot of approaches had to be considered for this part, since there was no dataset available for the hindi music notation, Devnagri Hindi Text Classification ended up being used and only selective elements, namely (सा रे गा मा प ध नि) were ended up getting passed to the model. These images are resized to 32px X 32px for uniformity, converted to binary as well and normalized.[4]

Data Augmentation is also used to add random flips, random rotation and random zoom to counter overfitting of the model. in addition to the normal Deep CNN model with max pooling, batch normalization, and adding multiple dense layers.



<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image17.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image17.png "image_tooltip")


**<span style="text-decoration:underline;">PART C</span> - **NOTATION CLASSIFICATION

The image array from PART A is used here to classify the acquired images from value 0 to 6 and then using a dictionary convert to Sa, Re, Ga, Ma, Pa, Dha, Ni and Saa. This array is then converted to stream using music21 library and converted to MIDI file and used as audio file.



4. 
Experiments


* **<span style="text-decoration:underline;">Trackbars for customized Width, Height and Aspect Ratio selection.</span>**

    Since this project was mainly carried out in Jupyter Notebooks, I ended up hard coding the values required for this particular image since Jupyter doesn’t allow interactive windows. But it was brought to my attention that these height and width values may not work on different images with smaller or larger text. So a commercial version of this project works, say for React or Android, i tried for an interface to which includes a trackbar inorder for the correct texts to be recognized.


    

<p id="gdcalert18" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image18.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert19">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image18.png "image_tooltip")


* **<span style="text-decoration:underline;">Iterative approach based on Pixel value threshold</span>**

    I ended up with an Contour detected based approach, but previously I was set on an Iterative based approach/ Sliding Window approach. I manually handpicked points on top left of the text necessarily and counted the number of pixels used to show that piece of text , i.e सा took 342 pixels on average,  रे took 275 pixels on average, गा 313 pixels on average, मा took 361 on average,  प took 256 and ध took 310. In short, in the 1600 X 1200 image, I planned to pick a 45 X 45 window on the top left and move it right and bottom and pass only those pixels that satisfy constraints based on these conditions. I was later made aware that my approach was fine but the implementation of it was somewhat naive. But by then, the contours based approach worked so I went with a contour based approach. This Pixels data with sliding window approach is still [here](https://github.com/mickee00000/201951090_Research_Internship_2022/blob/main/part1.csv).

* **<span style="text-decoration:underline;">Improving Datasets</span>**

    Since the dataset I received was somewhat different that the same I used the model on. E.g. not being able to read the works properly even after preprocessing.


    

<p id="gdcalert19" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image19.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert20">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image19.jpg "image_tooltip")
 


    _Sa getting classified as Maa._


    I fiddled around with the data set but the end solution is that the model needs to be trained using more of the text from the original sample to match.

* **<span style="text-decoration:underline;">Asking for too many output variables</span>:**

    There are a lot more variations of music notes in the bhatkhande notation system. When I added those into the mix I had to synthesize them using openCV, more precisely using open CV, horizontal lines and dots were drawn above and below these very same notations. The problem ended up being that the model accuracy plummeted in the test cases since it created a lot of confusion for the model to detect what notes are written in the sample image.

* **<span style="text-decoration:underline;">Testing on other notation images from the web</span>**

    Here only one problem arises, the constraint of hard coded values. For the searching purposes of the notes, a kernel size needs to be specified or in simpler words, consider the previous example of iterative a based approach in which a window size is decided upon to search in the whole document and fortunately this window size does not stay the same and changes based on document to document since this base example ’**_part1.jpeg_**’ is a high resolution 1600 X 1200 image whereas other examples are usually 360 X 360 or 480 X 480, resulting in different height and width thresholds.


    For filtering purposes too, certain conditions were applied as stated above, for example only the bounding rectangle of a certain size would be considered for prediction using the model but at least the size of the window needs to be calculated using trial and error method.




<p id="gdcalert20" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image20.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert21">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image20.png "image_tooltip")




<p id="gdcalert21" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image21.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert22">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image21.png "image_tooltip")




* **<span style="text-decoration:underline;">Trying to remove the meed node (a variation when another note is on top of a node adding that same variation)</span>**

    To remove this kind of note a lot of approaches had to be considered, few of them are:

* For the first approach it was observed that meed note are somewhat lesser in frequency, that's why all the coordinates of the notes were sorted by the y axis and a difference array was created to detect the horizontal frequency of the notes. unfortunately this did not plan out since frequency does not have anything to do with this variation. So in the cases that all notes have meed variation, the whole need row would be included and in the cases that the main notes are lesser in frequency would also be discarded.



<p id="gdcalert22" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image22.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert23">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image22.png "image_tooltip")




* Second approach was based on the principle of search by iteration, here for any note the area just above the note was passed into a function to search for any coordinates. Unfortunately this would only work if we know that the meed coordinate is directly above our current note but in actuality the meed can be found anywhere above the current note without any specific syntax for coordination.

     For a 2D based searching,searching would become a Tedious, resource expensive and time consuming task resulting in this approach to be discarded .

* Third was calculating the euclidean distance between the current note and the notes all above. This was the most bound to work approach and it did for the most part but in this case for any other test case it ends up getting stuck on the same problem of hard coded values. In other words, the minimum distance between two notes needs to be declared such that it is classified as a meed node..



<p id="gdcalert23" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image23.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert24">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image23.png "image_tooltip")


For all the earlier work, absolute properties of the notes were being modified and manipulated, like drawing rectangles around one note, allowing that rectangle to be included based on its physical properties, which is somewhat easier. The problem arises when relative positionings need to be processed in order for them to work, which is somewhat tricky and needs more experience to be handled properly.



* **<span style="text-decoration:underline;">Discarding the Handwritten Devanagari Dataset</span>**

    The model previously had a lot of issues with accuracy, mainly because the properties of handwritten and printed text are different and the possibility of misclassification increases exponentially. So to counter this issue, a custom dataset had to be generated by screenshotting and cropping text on written medium such as books and online images. Even though this process was tedious, it ended up making the model accuracy from 45.3239% to (current) 84.2105%, almost twice the original. This custom image dataset can be found [here](https://github.com/mickee00000/201951090_Research_Internship_2022/raw/main/Custom_notes_text.zip).


    

<p id="gdcalert24" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image24.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert25">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image24.png "image_tooltip")


* **<span style="text-decoration:underline;">Testing on Random Notation from the Internet</span>**

    The model needs to be sufficient enough to be used on any notation image that contains the notes. So to check that eligibility, 4 test cases were ran the results were promising.

* First classifications are made using the model.
* Then those values are checked one by one using an incremental iterator and the value is stored in an array/list in order to be cross checked against the predictions.
* After that, heat map and midi files are generated through these test cases resources and data of which can be found [here](https://github.com/mickee00000/201951090_Research_Internship_2022/tree/main/Efficiency%20Testing).

**<span style="text-decoration:underline;">TEST 1:</span>**

Problem Statement:



<p id="gdcalert25" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image25.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert26">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image25.jpg "image_tooltip")


Results:



<p id="gdcalert26" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image26.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert27">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image26.jpg "image_tooltip")




<p id="gdcalert27" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image27.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert28">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image27.png "image_tooltip")


Accuracy: **<span style="text-decoration:underline;">78.84%</span>**



<p id="gdcalert28" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image28.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert29">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image28.png "image_tooltip")


**<span style="text-decoration:underline;">TEST 2:</span>**

Problem Statement:



<p id="gdcalert29" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image29.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert30">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image29.jpg "image_tooltip")


Results:



<p id="gdcalert30" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image30.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert31">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image30.jpg "image_tooltip")




<p id="gdcalert31" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image31.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert32">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image31.png "image_tooltip")


Accuracy: **<span style="text-decoration:underline;">78.94%</span>**



<p id="gdcalert32" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image32.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert33">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image32.png "image_tooltip")


**<span style="text-decoration:underline;">TEST 3:</span>**

Problem Statement:



<p id="gdcalert33" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image33.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert34">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image33.jpg "image_tooltip")


Results: 



<p id="gdcalert34" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image34.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert35">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image34.jpg "image_tooltip")




<p id="gdcalert35" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image35.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert36">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image35.png "image_tooltip")


Accuracy: **<span style="text-decoration:underline;">69.3333%</span>**



<p id="gdcalert36" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image36.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert37">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image36.png "image_tooltip")


**<span style="text-decoration:underline;">TEST 4:</span>**

Problem Statement:



<p id="gdcalert37" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image37.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert38">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image37.jpg "image_tooltip")




<p id="gdcalert38" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image38.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert39">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image38.png "image_tooltip")




5. 
Conclusion
Only one two parameters were changed to achieve these results in the test (Search Window and Kernel Size) and once changed these parameters were kept the same for all the test cases(all 4). Accuracy could have been improved a lot, the new dataset really did wonders for this model, only hits taken by the accuracy were by the accidental detection of numbers as notes. If it were only the notes and not the number, the accuracy could have been above 90%. So, more tuning needs to be done in order of the hard coded values to be automatically computed instead of relying on the user input.

This project really made me aware of a lot more concepts in Machine Learning, Deep Learning and Image Manipulation. The best part about it is how different parts of this project do different things and it all comes together in the end ever so seamlessly. 


##### References

[1]  Alpaydin, E. (2021). _Machine Learning, revised and updated edition_. MIT Press.

[2]  _Canny edge detector_. OpenCV. (n.d.). Retrieved July 25, 2022, from https://docs.opencv.org/4.x/da/d5c/tutorial_canny_detector.html

[3]  Connectedreams.com. (2016, December 1). _Beginner's Guide to Computer Vision_. Medium. Retrieved July 25, 2022, from https://medium.com/readers-writers-digest/beginners-guide-to-computer-vision-23606224b720


    [4]  Kang, N. (2019, February 4). _Introducing deep learning and neural networks - deep learning for rookies (1)_. Medium. Retrieved July 25, 2022, from https://towardsdatascience.com/introducing-deep-learning-and-neural-networks-deep-learning-for-rookies-1-bd68f9cf5883


    [5]  Lee, S. (2022, January 30). _Lines detection with Hough Transform_. Medium. Retrieved July 25, 2022, from https://towardsdatascience.com/lines-detection-with-hough-transform-84020b3b1549


    [6]  Sha, P., & Dong, X. (2021, August 21). _Research on adolescents regarding the indirect effect of depression, anxiety, and stress between TikTok use disorder and memory loss_. International journal of environmental research and public health. Retrieved July 25, 2022, from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8393543/


    [7] Springer. (2014). Image Processing. In _Computer vision_. 
