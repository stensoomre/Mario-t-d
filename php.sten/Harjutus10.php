<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">

<div class="container">
<?php
$pages = array("Harjutus10_1", "Harjutus10_2", "Harjutus10_3", "Harjutus10_4");
$page = isset($_GET['page']) ? $_GET['page'] : "Harjutus10_1";

if (!in_array($page, $pages)) {
    die("Vabandame, sellist lehte ei eksisteeri.");
}

if (isset($_GET['logout'])) {
    session_destroy();
    header("Location: Harjutus10.php");
    exit();
}

if (!isset($_SESSION['logged_in'])) {
    $_SESSION['logged_in'] = false;
}

if (isset($_POST['username']) && isset($_POST['password'])) {
    if ($_POST['username'] == "admin" && $_POST['password'] == "parool") {
        $_SESSION['logged_in'] = true;
    } else {
        echo '<div class="alert alert-danger mt-4" style="height:60px" role="alert">Vale kasutajanimi või parool.';
    }
}

if (!$_SESSION['logged_in']) {
    ?>
    <form class= "container bg-primary bg-opacity-25 mt-4 text-black" action="" method="post">
        Kasutajanimi: <input class="m-1" type="text" name='username'><br>
        Parool: <input class="m-1" type="password" name="password"><br>
        <input type="submit" class="m-2 bg-success text-white" value="Logi sisse">
    </form>
    <?php
    exit();
}
?>

<div>
<a href="Harjutus10.php?page=Harjutus10_1">Leht 1</a> |
<a href="Harjutus10.php?page=Harjutus10_2">Leht 2</a> |
<a href="Harjutus10.php?page=Harjutus10_3">Leht 3</a> |
<a href="Harjutus10.php?page=Harjutus10_4">Leht 4</a>
<br><br>
</div>

<?php
switch ($page) {
    case "Harjutus10_1":
        include "Harjutus10_1.php";
        break;
    case "Harjutus10_2":
        include "Harjutus10_2.php";
        break;
    case "Harjutus10_3":
        include "Harjutus10_3.php";
        break;
    case "Harjutus10_4":
        include "Harjutus10_4.php";
        break;
}
?>

<br><br>
<a href="Harjutus10.php?logout=true">Logi välja</a>
</div>