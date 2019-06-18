import time
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail_sender():

    def __init__(self):
        self.to = None
        self.subject = None
        self.message = None
        self.gmail_sender = 'xxxxxxxxx@gmail.com'
        self.gmail_passwd = 'xxxxxxxxxxxxxx'
        self.content = None
        self.preamble = """ \
                        Your mail reader does not support the report format.\
                        Please visit us <a href="http://www.pea.co.th">online</a>!\
                        """
        

    def preparation(self, reciver, subject):

        self.to = reciver
        self.subject = subject

    def login(self):
       
        try :
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(self.gmail_sender, self.gmail_passwd)
            return(True)
        except Exception as err:
            print(err)
            return(False)


    def send(self, msg="This is Default Body Message"):
        
        # self.body = '\r\n'.join(['To: %s' % self.to,
        #                 'From: %s' % self.gmail_sender,
        #                 'Subject: %s' % self.subject,
        #                 '', msg])


        self.html_body = MIMEText(msg,'html')

        MESSAGE = MIMEMultipart('alternative')
        MESSAGE.set_charset("utf-8")
        MESSAGE['subject'] = self.subject
        MESSAGE['To'] = self.to
        MESSAGE['From'] = self.gmail_sender
        MESSAGE.preamble = self.preamble
        MESSAGE.attach(self.html_body)

        try:
            self.server.sendmail(self.gmail_sender, [self.to], MESSAGE.as_string())
            print ('email sent')
            return True
        except Exception as err :
            print ('error sending mail: {}'.format(err))
            return False

        
    def logout(self): 
        self.server.quit()

if __name__ == "__main__":

    # todo : create html template reader to content here
    
    content = """
                    <title>W3.CSS Template</title>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
                        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
                        <style>
                        body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
                        </style>
                        <body class="w3-light-grey">

                        <!-- w3-content defines a container for fixed size centered content, 
                        and is wrapped around the whole page content, except for the footer in this example -->
                        <div class="w3-content" style="max-width:1400px">

                        <!-- Header -->
                        <header class="w3-container w3-center w3-padding-32"> 
                        <h1><b>MY BLOG</b></h1>
                        <p>Welcome to the blog of <span class="w3-tag">unknown</span></p>
                        </header>

                        <!-- Grid -->
                        <div class="w3-row">

                        <!-- Blog entries -->
                        <div class="w3-col l8 s12">
                        <!-- Blog entry -->
                        <div class="w3-card-4 w3-margin w3-white">
                            <img src="/w3images/woods.jpg" alt="Nature" style="width:100%">
                            <div class="w3-container">
                            <h3><b>TITLE HEADING</b></h3>
                            <h5>Title description, <span class="w3-opacity">April 7, 2014</span></h5>
                            </div>

                            <div class="w3-container">
                            <p>Mauris neque quam, fermentum ut nisl vitae, convallis maximus nisl. Sed mattis nunc id lorem euismod placerat. Vivamus porttitor magna enim, ac accumsan tortor cursus at. Phasellus sed ultricies mi non congue ullam corper. Praesent tincidunt sed
                                tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.</p>
                            <div class="w3-row">
                                <div class="w3-col m8 s12">
                                <p><button class="w3-button w3-padding-large w3-white w3-border"><b>READ MORE »</b></button></p>
                                </div>
                                <div class="w3-col m4 w3-hide-small">
                                <p><span class="w3-padding-large w3-right"><b>Comments  </b> <span class="w3-tag">0</span></span></p>
                                </div>
                            </div>
                            </div>
                        </div>
                        <hr>

                        <!-- Blog entry -->
                        <div class="w3-card-4 w3-margin w3-white">
                        <img src="/w3images/bridge.jpg" alt="Norway" style="width:100%">
                            <div class="w3-container">
                            <h3><b>BLOG ENTRY</b></h3>
                            <h5>Title description, <span class="w3-opacity">April 2, 2014</span></h5>
                            </div>

                            <div class="w3-container">
                            <p>Mauris neque quam, fermentum ut nisl vitae, convallis maximus nisl. Sed mattis nunc id lorem euismod placerat. Vivamus porttitor magna enim, ac accumsan tortor cursus at. Phasellus sed ultricies mi non congue ullam corper. Praesent tincidunt sed
                                tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.</p>
                            <div class="w3-row">
                                <div class="w3-col m8 s12">
                                <p><button class="w3-button w3-padding-large w3-white w3-border"><b>READ MORE »</b></button></p>
                                </div>
                                <div class="w3-col m4 w3-hide-small">
                                <p><span class="w3-padding-large w3-right"><b>Comments  </b> <span class="w3-badge">2</span></span></p>
                                </div>
                            </div>
                            </div>
                        </div>
                        <!-- END BLOG ENTRIES -->
                        </div>

                        <!-- Introduction menu -->
                        <div class="w3-col l4">
                        <!-- About Card -->
                        <div class="w3-card w3-margin w3-margin-top">
                        <img src="/w3images/avatar_g.jpg" style="width:100%">
                            <div class="w3-container w3-white">
                            <h4><b>My Name</b></h4>
                            <p>Just me, myself and I, exploring the universe of uknownment. I have a heart of love and a interest of lorem ipsum and mauris neque quam blog. I want to share my world with you.</p>
                            </div>
                        </div><hr>
                        
                        <!-- Posts -->
                        <div class="w3-card w3-margin">
                            <div class="w3-container w3-padding">
                            <h4>Popular Posts</h4>
                            </div>
                            <ul class="w3-ul w3-hoverable w3-white">
                            <li class="w3-padding-16">
                                <img src="/w3images/workshop.jpg" alt="Image" class="w3-left w3-margin-right" style="width:50px">
                                <span class="w3-large">Lorem</span><br>
                                <span>Sed mattis nunc</span>
                            </li>
                            <li class="w3-padding-16">
                                <img src="/w3images/gondol.jpg" alt="Image" class="w3-left w3-margin-right" style="width:50px">
                                <span class="w3-large">Ipsum</span><br>
                                <span>Praes tinci sed</span>
                            </li> 
                            <li class="w3-padding-16">
                                <img src="/w3images/skies.jpg" alt="Image" class="w3-left w3-margin-right" style="width:50px">
                                <span class="w3-large">Dorum</span><br>
                                <span>Ultricies congue</span>
                            </li>   
                            <li class="w3-padding-16 w3-hide-medium w3-hide-small">
                                <img src="/w3images/rock.jpg" alt="Image" class="w3-left w3-margin-right" style="width:50px">
                                <span class="w3-large">Mingsum</span><br>
                                <span>Lorem ipsum dipsum</span>
                            </li>  
                            </ul>
                        </div>
                        <hr> 
                        
                        <!-- Labels / tags -->
                        <div class="w3-card w3-margin">
                            <div class="w3-container w3-padding">
                            <h4>Tags</h4>
                            </div>
                            <div class="w3-container w3-white">
                            <p><span class="w3-tag w3-black w3-margin-bottom">Travel</span> <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">New York</span> <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">London</span>
                            <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">IKEA</span> <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">NORWAY</span> <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">DIY</span>
                            <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">Ideas</span> <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">Baby</span> <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">Family</span>
                            <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">News</span> <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">Clothing</span> <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">Shopping</span>
                            <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">Sports</span> <span class="w3-tag w3-light-grey w3-small w3-margin-bottom">Games</span>
                            </p>
                            </div>
                        </div>
                        
                        <!-- END Introduction Menu -->
                        </div>

                        <!-- END GRID -->
                        </div><br>

                        <!-- END w3-content -->
                        </div>
    """
    adaptor = Mail_sender()
    adaptor.preparation(reciver="xxxxxxxx@gmail.com", subject="Invite to register Our Reference Price Website") 
    if adaptor.login():
        if adaptor.send(msg=content) :
            adaptor.logout() 
        else :
            print("Can not Send your E-mail")
    else:
        print("Can not to sign in to Google Mail Server")
    