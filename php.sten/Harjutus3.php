<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Harjutus 3</title>
</head>

<body>
    <?php
    //Sten Soomre Harjutus 2 Sten Soomre 24.01.2023
    $toode1 = intval($_GET['t1']);
    $toode2 = intval($_GET['t2']);
    $toode3 = intval($_GET['t3']);
    $vaste1 = $toode1 + $toode2;
    $vaste1 = $vaste1 / 2;
    $vaste1 = $vaste1 * $toode3;
    $vaste2 = $toode1 * $toode3;

    echo "Trapetsi pindala: ($toode1+$toode2)/2*$toode3 = $vaste1<br>";
    echo "Rombi pindala: $toode1*$toode3 = $vaste2<br>";
    ?>
</body>

</html>