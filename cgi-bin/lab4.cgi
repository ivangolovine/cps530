#!/usr/bin/perl
use CGI':standard';
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
print "Content-type: text/html\n\n";

print "<!DOCTYPE html>";
print "<html><head>";
print "<title> Lab 4 </title>";
print "<meta name='viewport' content='width=device-width, initial-scale=1'>";
print "<link rel='preconnect' href='https://fonts.googleapis.com'>";
print "<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>";
print "<link href='https://fonts.googleapis.com/css2?family=Explora&display=swap' rel='stylesheet'>";
print "</head>";
print "<body>";
print '<div style = "color:blue; 
    font-family: Explora; font-size: 4em; text-align: center; margin-left: auto;
    margin-right: auto;
    width: 8em;">This is my first Perl program</div>';
print "</body></html>";
