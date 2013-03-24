<html>
<head>
	<title>Mike Lyons - Software Engineer</title>

	<link href='http://fonts.googleapis.com/css?family=Fjalla+One' rel='stylesheet' type='text/css'>
	<link href='http://fonts.googleapis.com/css?family=Shanti' rel='stylesheet' type='text/css'>

	<link href='reset.css' rel='stylesheet' type='text/css'>
	<link href='main.css' rel='stylesheet' type='text/css'>
	<link href='top_contentbox.css' rel='stylesheet' type='text/css'>

	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
	<script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.0/jquery-ui.min.js"></script>

	<script src="main_script.js"></script>
</head>
<body>
	<div id="body">
		<div id="menu_area">
			<div class="title" id="name">
				M<a id="i">i</a>ke Lyons  
			</div>
			<div id="menu">
				<a class="nav_link" id="aboutme" href="../">
					About Me
				</a>
				<a class="nav_link" id="projects" href="../projects.php">
					Projects
				</a>
				<a class="nav_link" id="contact" href="../construction.php">
					Contact
				</a>
			</div>
		</div>
		<div id="content_area">
			<div class="content">
				<form action="index.php" method="post">
					Paste url of JavaDoc page here:
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
			</div>
		</div>
		<div id="ibox" class="content">
			Renee is awesome
		</div>
	</div>
</body>
</html>