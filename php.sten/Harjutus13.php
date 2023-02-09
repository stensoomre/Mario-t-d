<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Harjutus 13</title>
</head>

<body>
    <?php
    //Sten Soomre Harjutus 13 Sten Soomre 09.02.2023
    if (isset($_POST['submit'])) {
        $errors = array();
        $file_name = $_FILES['file']['name'];
        $file_size = $_FILES['file']['size'];
        $file_tmp = $_FILES['file']['tmp_name'];
        $file_type = $_FILES['file']['type'];
        $file_parts = explode('.', $_FILES['file']['name']);
        $file_ext = strtolower(end($file_parts));
        
        $expensions = array("jpeg", "jpg");

        if (in_array($file_ext, $expensions) === false) {
            $errors[] = "Lubatud on ainult JPEG ja JPG formaadis failid.";
        }

        if ($file_size > 2097152) {
            $errors[] = 'Faili suurus peab olema alla 2 MB';
        }

        if (empty($errors) == true) {
            move_uploaded_file($file_tmp, "uploads/" . $file_name);
            echo "Üleslaadimine õnnestus: " . "uploads/" . $file_name;
        } else {
            print_r($errors);
        }
    }
    ?>
    <html>

    <body>

        <form action="" method="POST" enctype="multipart/form-data">
            <input type="file" name="file" />
            <input type="submit" value="Laadi üles" name="submit" />
        </form>

    </body>
    <html>

    <body>
        <form action="" method="POST" enctype="multipart/form-data">
            <input type="file" name="file" />
            <input type="submit" value="Laadi üles" name="submit" />
        </form>
        <h2>Üleslaaditud pildid:</h2>
        <?php
        $files = glob("uploads/*.*");
        for ($i = 0; $i < count($files); $i++) {
            $num = $files[$i];
            echo '<a href="' . $num . '" target="_blank"><img src="' . $num . '" width="200" /></a>';
        }
        ?>
    </body>

    </html>