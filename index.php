<form action="index.php" method="post">
<img src="cpp.png" alt="Are you happy now Grace?!"/><br />
<textarea rows="18" cols="110" name="note">
<?php
if (!$_POST["note"] == "")
{
	$writeFile = fopen("test.cpp","w");
	$newStat =  $_POST["note"];
	fwrite($writeFile,$newStat);
	fclose($writeFile);
	passthru('uncrustify -c /home/alkaline/share/beauty/config.cfg -f /home/alkaline/share/beauty/test.cpp -o /home/alkaline/share/beauty/test.cpp');
	passthru('/home/alkaline/share/beauty/log.sh');



$file = fopen("test.cpp","r");
while(!feof($file))
  {
  echo fgets($file);
  }
fclose($file);
}
?>
</textarea>
<br /> 
<input type="submit" width="100" value="go" />
</form>