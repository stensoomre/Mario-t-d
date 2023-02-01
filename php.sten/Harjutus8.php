<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>

<body>

    <div class="container mt-5">
        <h2 class="text-center">Harjutus 8</h2>
        <hr>
        <div class="row">
            <div class="col-md-6 mb-3">
                <?php
                $date = new DateTime('2023-03-20 17:31');
                echo $date->format('d.m.Y H:i') . "<br>";
                ?>
            </div>
            <div class="col-md-6 mb-3">
                <form>
                    <div class="form-group">
                        <label for="birthyear">Sisesta oma sünniaasta:</label>
                        <input type="text" class="form-control" id="birthyear" name="birthyear">
                    </div>
                    <button type="submit" class="btn btn-primary">Arvuta</button>
                </form>
                <?php
                if (isset($_GET['birthyear'])) {
                    $birthyear = $_GET['birthyear'];
                    $birthdate = new DateTime($birthyear . '-01-01');
                    $today = new DateTime();
                    $interval = $today->diff($birthdate);
                    echo '<div class="alert alert-success mt-4" role="alert">Olete ' . $interval->y . ' aastat vana.<br></div>';
                }
                ?>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6 mb-3">
                <?php
                //Sten Soomre Harjutus 6 Sten Soomre 01.03.2023
                $endOfYear = new DateTime('2023-06-30');
                $today = new DateTime();
                $interval = $today->diff($endOfYear);
                echo 'Kooliaasta lõpuni on jäänud ' . $interval->format('%a päeva<br>');
                ?>
            </div>
            <div class="col-md-6 mb-3">
                <?php
                $date = new DateTime();
                $month = $date->format('m');

                if ($month >= 3 && $month <= 5) {
                    echo '<img src="/php.sten/img/autumn.png">';
                } elseif ($month >= 6 && $month <= 8) {
                    echo '<img src="/php.sten/img/summer.png">';
                } elseif ($month >= 9 && $month <= 11) {
                    echo '<img src="/php.sten/img/spring.png">';
                } else {
                    echo '<img src="/php.sten/img/winter.png">';
                }
                ?>
            </div>

        </div>
    </div>
</body>

</html>