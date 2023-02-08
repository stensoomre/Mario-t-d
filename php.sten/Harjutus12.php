<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <title>Harjutus 12</title>
</head>

<body>
    <div class="container">
        <h1>Harjutus 12</h1>
        <hr>
        <div class="row">
            <div class="col-sm-6">
                <form action="" method="post">
                    <input type="text" class="form-control" id="aeg1" name="aeg1" required>
                    <label>Start aeg (00:00)</label>
                    <input type="text" class="form-control mt-4" id="aeg2" name="aeg2" required>
                    <label>Lõpp aeg (24:00)</label>

            </div>
            <div class="col-sm-6">
                <button type="submit" class="btn btn-success">Arvuta</button>
                </form>

                <?php
                //Sten Soomre Harjutus 12 Sten Soomre 08.02.2023

                if (isset($_POST['aeg1']) && isset($_POST['aeg2'])) {
                    $aeg1 = $_POST['aeg1'];
                    $aeg2 = $_POST['aeg2'];
                    if (strlen($aeg1) == 5){
                        if (strlen($aeg2) == 5){
                          echo '<div class="alert alert-success mt-4" role="alert">Olete ' . $aeg1 . ' aastat vana.<br></div>';
                        }
                      } else {
                        echo '<div class="alert alert-danger mt-4" role="alert">Start aeg väli on vigane!<br></div>';
                      }
                    } else {
                      echo '<div class="alert alert-danger mt-4" role="alert">Lõpp aeg väli on vigane!<br></div>';
                    }
                ?>
            </div>
        </div>
</body>

</html>