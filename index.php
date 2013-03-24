Paste JavaDoc page source here:
<form action="index.php" method="post">
<input type="text" name="url" /><br/>
<textarea rows="18" cols="110" width=100% name="note">
<?php
$haveDoc = false;
$docLocation = "";

if (isset($_POST["note"]))
{
	$writeFile = fopen("temp.txt","w");
	$newStat =  $_POST["note"];
	fwrite($writeFile,$newStat);
	fclose($writeFile);
	$haveDoc = true;
	$docLocation = "temp.txt";
}

if (isset($_REQUEST["url"]))
{
	$url_file = file_get_contents($_REQUEST["url"]);

	shell_exec("touch downloads/" + $_REQUEST["url"]);

	$writeFile = fopen("temp.txt","w");
	$newStat =  $url_file;
	fwrite($writeFile,$newStat);
	fclose($writeFile);
	$haveDoc = true;
	$docLocation = "temp.txt";
}

if( $haveDoc && $docLocation != "" )
{
	echo passthru('./ReverseDoc.py < ' + $docLocation + ' > temp.java');

	$file = fopen("temp.java","r");
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
