# <font color='brown' size='21px' weight='bold'>  **WhatsApp-Group-Chat-Analysis-Dashboard** </font>

## Table of Contents
<ul>
<li><a href="#intro">Introduction</a></li>
<li><a href="#extraction">Data Extraction</a></li>
<li><a href="#wrangling">Data Wrangling</a></li>
<li><a href="#eda">Exploratory Data Analysis</a></li>
<li><a href="#conclusions">Conclusions</a></li>
</ul>



<a id='intro'></a>
## <font size='15px' weight='bold'> **Introduction** </font>
   
WhatsApp-Group-Chat-Analyser is a web-based dashboard for PCs only that is used to display the analysis of your WhatsApp Group Chats.

WhatsApp has become one of the most trendy social media platform. WhatsApp Chat Analyzer means is a platform that tracks our conversation and analyses group activities and how much time we
are spending  on WhatsApp. 

**Interface**

<img src="Images\FrontShow.jpg" alt='Demo Image' style=" width:960px ; "  >


<a id='extraction'></a>
## <font size='15px' weight='bold'> **Data Extraction** </font>

WhatsApp provides us the feature of exporting chats. The steps to export the chat and save the file is illustrated by the diagram below.
Following that, create a python program that will extract the Date, Username of Author, Time, Messages from exported chat file and creating a data frame for its storage.

The steps are as follows:
> - Navigate to the desired group chat (in this case Tech tricks Kenya) and locate the 3 dots at the menu bar.
> - Select `more` from the drop down list.
> - Then select `Export Chart` from the resulting drop down list.
> - Then export chats without media.

<img src="Images\Extraction Steps.png" alt='Extraction Steps' style=" width:960px ; "  >


The required python libraries for the extraction of useful information from raw whatsapp data data is listed in the [requirements.txt file](requirements.txt)

<a id='wrangling'></a>
## Data Wrangling

The data to be cleansed is stored as `extractedData.csv`. 

#### Data Understanding

To understand this data, I seek to answer the following questions:
    
> - How many active participants are in the group?

> - How many texts and media have been sent to the group?

> - What are the commonly used words in the group chat.

> - What are the emotions attached to every user?

> - What are the trends in chatting in the group?