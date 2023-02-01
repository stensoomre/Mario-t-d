<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
        integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
        integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV"
        crossorigin="anonymous"></script>
    <h1>Harjutus 04</h1>
</head>

<body>

    <div class="container">
        <h1 class="mg-4">Jagamine</h1>
        <form action="" method="get" class="form-group">
            <label for="number1">Sisesta esimene arv:</label>
            <input type="text" name="number1" class="form-control">
            <label for="number2">Sisesta teine arv:</label>
            <input type="text" name="number2" class="form-control">
            <h1>Vanuse võrdlus</h1>
            <label for="age1">Sisesta esimene vanus:</label>
            <input type="text" name="age1" class="form-control">

            <label for="age2">Sisesta teine vanus:</label>
            <input type="text" name="age2" class="form-control">
            <input type="submit" value="Jaga" class="btn btn-primary mt-3">
        </form>

        <form action="" method="get" class="form-group">
            <h1>Ristkülik või Ruut</h1>
            <label for="length">Sisesta ristküliku pikkus:</label>
            <input type="text" name="length" class="form-control">
            <label for="width">Sisesta ristküliku laius:</label>
            <input type="text" name="width" class="form-control">
            <input type="submit" value="Otsusta" class="btn btn-primary mt-3">
        </form>
        <?php
        if (isset($_GET['length']) && isset($_GET['width'])) {
            $length = $_GET['length'];
            $width = $_GET['width'];
            if ($length == $width) {
                echo "<div class='alert alert-info'>See on ruut.</div>";
            } else {
                echo "<div class='alert alert-info'>See on ristkülik.</div>";
            }
        }
        ?>

        <?php
            //Sten Soomre Harjutus 4 Sten Soomre 31.01.2023
        if (isset($_GET['number1']) && isset($_GET['number2']) && isset($_GET['age1']) && isset($_GET['age2'])) {
            $number1 = $_GET['number1'];
            $number2 = $_GET['number2'];
            if ($number2 == 0) {
                echo "<div class='alert alert-warning'>HOIATUS: Ära jaga nulliga!!</div>";
            } else {
                $result = $number1 / $number2;
                echo "<div class='alert alert-success'>Tulemus: " . $result . "</div>";
            }
            $age1 = $_GET['age1'];
            $age2 = $_GET['age2'];
            if ($age1 > $age2) {
                echo "<div class='alert alert-info'>Esimene vanus on vanem.</div>";
            } elseif ($age1 < $age2) {
                echo "<div class='alert alert-info'>Teine vanus on vanem.</div>";
            } elseif ($age1 == $age2) {
                echo "<div class='alert alert-info'>Vanused on samad.</div>";
            }
        }
        ?>

        <form action="" method="get" class="form-group">
            <h1>Sünniaasta juubeli kontroll</h1>
            <label for="birthyear">Sisesta sünniaasta:</label>
            <input type="text" name="birthyear" class="form-control">
            <input type="submit" value="Kontrolli" class="btn btn-primary mt-3">
        </form>
        <?php
        if (isset($_GET['birthyear']) && !empty($_GET['birthyear'])) {
            $birthyear = $_GET['birthyear'];
            $currentyear = date("Y");
            $age = $currentyear - $birthyear;
            if ($age % 5 == 0) {
                echo "<div class='alert alert-info'>See on juubeliaasta.</div>";
            } else {
                echo "<div class='alert alert-info'>See ei ole juubeliaasta.</div>";
            }
        }
        ?>

        <form action="" method="get" class="form-group">
            <h1>KT punktid</h1>
            <label for="points">Sisesta oma KT punktid:</label>
            <input type="text" name="points" class="form-control">
            <input type="submit" value="Sisesta" class="btn btn-primary mt-3">
        </form>

        <?php
        if (isset($_GET['points'])) {
            $points = $_GET['points'];
            if (is_numeric($points)) {
                if ($points >= 10) {
                    echo "<div class='alert alert-success'>SUPER!</div>";
                } elseif ($points >= 5 && $points <= 9) {
                    echo "<div class='alert alert-info'>TEHTUD!</div>";
                } elseif ($points < 5) {
                    echo "<div class='alert alert-warning'>KASIN!</div>";
                }
            } else {
                echo "<div class='alert alert-warning'>SISESTA OMA PUNKTID!</div>";
            }
        }
        ?>

    </div>

</body>

</html>