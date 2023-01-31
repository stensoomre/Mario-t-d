<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</head>

<body>
    <div class="container">
        <form action="" method="get" class="form-group">
            <h1>Jagamine</h1>
            <label for="number1">Sisesta esimene arv:</label>
            <input type="text" name="number1" class="form-control">
            <label for="number2">Sisesta teine arv:</label>
            <input type="text" name="number2" class="form-control">
            <h1>Vanusevõrdlus</h1>
            <label for="age1">Sisesta esimene vanus:</label>
            <input type="text" name="age1" class="form-control">
            <label for="age2">Sisesta teine vanus:</label>
            <input type="text" name="age2" class="form-control">
            <input type="submit" value="Jaga" class="btn btn-success mt-4">
        </form>
        <?php
        if (isset($_GET['number1']) && isset($_GET['number2']) && isset($_GET['age1']) && isset($_GET['age2'])) {
            $number1 = $_GET['number1'];
            $number2 = $_GET['number2'];
            if ($number2 == 0) {
                echo "<div class='alert alert-warning'>HOIATUS: Nulliga jagamine on võimatu!</div>";
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
                echo "<div class='alert alert-info'>Vanused on ühevanused.</div>";
            }
        }
        ?>
    </div>

</body>

</html>