Paste url of JavaDoc page here:
<form action="index.php" method="post">
<input type="text" name="url" style="width:600px;"/><br/>
Code comes out here:<br/>
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

	$writeFile = fopen("temp.txt","w");
	$newStat =  $url_file;
	fwrite($writeFile,$newStat);
	fclose($writeFile);
	$haveDoc = true;
	$docLocation = "temp.txt";
}

if( $haveDoc && $docLocation != "" )
{
	# shell_exec('ReverseDoc.py < temp.txt > temp.java');
	passthru( "./runReverseDoc.sh" );

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
