#!/usr/bin/perl
use CGI':standard';
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);


print "Content-type: text/html\n\n";

#$fn = param ('first');
$firstName = param ('firstName');
$lastName = param ('lastName');
$streetName = param ('streetName');
$city = param ('city');
$postalCode = param ('postalCode');
$province = param ('province');
$gender = param ('gender');
$phone = param ('phone');
$email = param ('email');
$password = param ('password');

#validate email
my $regex = $email =~ /^[a-z0-9.]+\@[a-z0-9.-]+$/;
my $phoneregex = $phone =~ /^[0-9]+$/;

if (length($postalCode) != 6) {
    print qq(<p style = "color: red;background: rgba(255, 122, 89, .5);"> Invalid Postal Code Click Return To Form</p>);
}
if (not $regex){
    #print qq(<meta http-equiv="refresh" content="1;url=https://www2.cs.ryerson.ca/~igolovin/cgi-bin/lab4form3.cgi" />);
    print qq(<p style = "color: red; background: rgba(255, 122, 89, .5);"> Invalid Email Click Return To Form</p>);
}
if (not $phoneregex or length($phone) != 10){
    print qq(<p style = "color: red; background: rgba(255, 122, 89, .5);"> Invalid Phone Click Return To Form</p>);
}

print <<"HTML CONTENT";
<html><head>
<title> Lab 4 </title>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<link rel='preconnect' href='https://fonts.googleapis.com'>
<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>
<link href='https://fonts.googleapis.com/css2?family=Explora&display=swap' rel='stylesheet'>
<link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">
<style>
html, body {
	font-family: Roboto, sans-serif;
	font-size: 16px;
	text-align: center;
	scroll-behaviour: smooth;
}
#main {
	height: auto;
    width: 625px;
    margin: 12px auto;
    background: #88be8c;
    padding: 1px;
    box-shadow: 0 0 12px rgba(0,0,0,.1);
    border-radius: 16px;
	transition: ease all 0.25s;
}
#inform {
	padding-left: 200px;
	text-align: left;
}

#topname {
    color:blue; 
    font-family: Explora, sans-serif; font-size: 4em; text-align: center; margin-left: auto;
    margin-right: auto;
    width: 8em;
    }

.popup:hover {
     transform: scale(1.10);
     transition: 0.20s 
}
.button {
    	border-radius: 8px;
     	border: none;
	    background-color: dimgrey;
	    color: white;
     	font-size: 14px;
     	text-align: center;
     	padding: 10px 15px;
     	cursor: pointer;
}
.button:hover {
     	background-color: grey;
}
</style>
</head>
<body>
<div id="topname">Form Lab 4</div>
<div id="main">
<h3>Submitted information:</h3>
<div id="inform">
First Name:$firstName<br>
Last Name:$lastName<br>
Gender:$gender<br>
Phone Number:$phone<br>
Email:<a href="mailto:$email">$email</a><br>
Street Name:$streetName<br>
City:$city<br>
Postal Code:$postalCode<br>
Province:$province<br><br>
</div>
<br><br>
</div>
<button class="popup button" onclick="window.location.href = 'https://www2.cs.ryerson.ca/~igolovin/cgi-bin/lab4form3.cgi';">Return To Form</button>
<br><br>
</div>
</body>
</html>
HTML CONTENT


