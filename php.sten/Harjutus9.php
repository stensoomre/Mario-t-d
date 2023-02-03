<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">  <title>PHP Code to HTML</title>
</head>
<body>
<div class="container my-5 bg-primary bg-opacity-25 border border-secondary">
  <?php
    $input = "mARiO";
    $name = ucfirst(strtolower($input));
    echo "<h1>Tere, " . $name . "!</h1>";
    $input = "stalker";
    $output = "";
    for ($i = 0; $i < strlen($input); $i++) {
      $output .= strtoupper($input[$i]) . ".";
    }
    echo "<p>" . $output . "</p>";
    $input = "Sa oled täielik noob";
    $bannedWords = array("noob");
    $output = $input;
    foreach ($bannedWords as $word) {
      $stars = str_repeat("*", strlen($word));
      $output = str_replace($word, "***", $output);
    }
    echo "<p>" . $output . "</p>";
    $firstName = "ülle";
    $lastName = "Doos";
    $email = strtolower(preg_replace('/[^A-Za-z0-9\.\_\-]/', '', iconv('UTF-8', 'ASCII//TRANSLIT', $firstName))) . "." . strtolower(preg_replace('/[^A-Za-z0-9\.\_\-]/', '', iconv('UTF-8', 'ASCII//TRANSLIT', $lastName))) . "@hkhk.edu.ee";

    echo "<p>" . $email . "</p>";
  ?>
</div>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
