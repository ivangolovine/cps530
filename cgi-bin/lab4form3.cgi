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
print qq(<style> html, body {
	font-family: Roboto, sans-serif;
	font-size: 16px;
	text-align: center;
	scroll-behaviour: smooth;
    background: #88be8c;}
    
    #topname {
    color:blue; 
    font-family: Explora, sans-serif; font-size: 4em; text-align: center; margin-left: auto;
    margin-right: auto;
    width: 8em;
    }

</style>);
print "</head>";
print "<body>";
print '<div id="topname">This is my first Perl program</div>';
#form creation attempt
print qq(<form method = "post" action ="https://www2.cs.ryerson.ca/~igolovin/cgi-bin/lab4pt2.cgi">);
print qq(<h4>Please Enter Your First and Lastname</h4>);
print qq(<p>First name: <input name = "firstName" type = "text" size = "20"></p>);
print qq(<p>Last name: <input name = "lastName" type = "text" size = "20"></p>);
print qq(<br>);
print qq(<h4>Please Enter address</h4>);
print qq(<p>Street name: <input name = "streetName" type = "text" size = "20"></p>);
print qq(<p>City: <input name = "city" type = "text" size = "20"></p>);
print qq(<p>Postal Code: <input name = "postalCode" type = "text" size = "20"></p>);
print qq(<br>);
print qq(<div><label for="province">Choose a Province:</label></div>);
print qq(<select name="province" id="province">
        <optgroup label="Provinces">
        <option value="AL">Alberta</option>
        <option value="BC">British Columbia</option>
        <option value="MT">Manitoba</option>
        <option value="NB">New Brunswick</option>
        <option value="NFL">Newfoundland and Labrador</option>
        <option value="NS">Nova Scotia</option>
        <option value="ON">Ontario</option>
        <option value="PEI">Prince Edward Island</option>
        <option value="QB">Quebec</option>
        <option value="SC">Saskatchewan</option>
        </optgroup>
        <optgroup label="Territories">
        <option value="NT">Northwest Territories</option>
        <option value="NV">Nunavut</option>
        <option value="YK">Yukon</option>
        </optgroup>
        </select>);
print qq(<br>);
print qq(<h4>Gender</h4>);
print qq(<p> Male: <input type="radio" name="gender" value="M">
        Female: <input type="radio" name="gender" value="F">
        Other: <input type="radio" name="gender" value="O"> </p>);
print qq(<br>);
print qq(<p>Phone number: <input name = "phone" type = "text" size = "20"></p>);
print qq(<p>Email address: <input name = "email" type = "text" size = "20"></p>);
print qq(<p>Password: <input type="password" name = "password" style = "width:200px"></p>);
print qq(<p><input type="submit" value="Submit"></p>);
print qq(<input type = "reset" value = "reset">);
print qq(</form>);
print "</body></html>";


