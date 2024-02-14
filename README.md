# Password Strength Checker

The purpose of this project is to to evaluate the strength of passwords. With this tool, you can make sure your passwords are safe from potential cracking attacks.

<strong>Functionality:</strong>
<ul data-sourcepos="5:1-8:70">
<span>
</span><li data-sourcepos="5:1-5:60"><span>It prompts the user to enter a password in an entry field.</span></li><span>
</span><li data-sourcepos="6:1-8:70"><span>It checks the password strength based on:</span><span>
</span><ul data-sourcepos="7:5-8:70"><span>
</span><li data-sourcepos="7:5-7:48"><strong>Length:</strong><span> Must be at least 8 characters.</span></li><span>
</span><li data-sourcepos="8:5-8:70"><strong>Character types:</strong><span> Must contain at least one uppercase letter,</span><span> lowercase letter,</span><span> digit,</span><span> and special character.</span></li><span>
</span></ul><span>
</span></li><span>
</span><li data-sourcepos="9:1-10:25"><span>Based on the criteria,</span><span> it displays a message box:</span><span>
</span><ul data-sourcepos="10:5-10:25"><span>
</span><li data-sourcepos="10:5-10:25"><span>Strong password:</span><span> If all criteria are met and length is &gt;= 10.</span></li><span>
</span><li data-sourcepos="11:5-11:83"><span>Medium strength password:</span><span> If all criteria are met but length is less than 10.</span></li><span>
</span></ul><span>
</span></li><span>
</span></ul>
<br>
The graphical interface of the password strength checker is as follows:<br>
<br>
<img alt="" class="bg hc hd c" width="500" height="150" loading="lazy" role="presentation" src="https://i.ibb.co/3SjX0fp/pswd-Checker.png"></img>


# Results
<ol> 
  <li>When password is of less than 8 characters :</li>
  <img alt="" class="bg hc hd c" width="450" height="250" loading="lazy" role="presentation" src="https://i.ibb.co/6rmkyDQ/Eightcharmissing.png"></img><br></br>
  
  <li>After satisfying the above condition, when password does not contain an upper case letter :</li>
  <img alt="" class="bg hc hd c" width="450" height="250" loading="lazy" role="presentation" src="https://i.ibb.co/J3FrmnC/UCM.png"></img><br></br>
  
  <li>After satisfying the above conditions, when password does not contain a lower case letter :</li>
  <img alt="" class="bg hc hd c" width="450" height="250" loading="lazy" role="presentation" src="https://i.ibb.co/N3NJKWX/LCM.png"></img><br></br>
  
  <li>After satisfying the above conditions, when password does not contain a special character :</li>
  <img alt="" class="bg hc hd c" width="450" height="250" loading="lazy" role="presentation" src="https://i.ibb.co/BLJx08b/SCM.png"></img><br></br>
  
  <li>After satisfying all the above conditions, the output of the 8 character password is as follows:</li>
  <img alt="" class="bg hc hd c" width="450" height="250" loading="lazy" role="presentation" src="https://i.ibb.co/G7b1btm/8CMP.png"></img><br></br>

  <li>Further in a 10 character password satisfying the first four conditions, the output is as follows:</li>
  <img alt="" class="bg hc hd c" width="350" height="200" loading="lazy" role="presentation" src="https://i.ibb.co/kQhZMzT/10CSP.png"></img><br></br>
  <strong>Note:</strong> This output is applicable for any password with a minimum of 10 characters satisfying the parameters.
  
</ol>
