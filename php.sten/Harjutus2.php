<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Harjutus 2</title>
</head>
<body>
    <?php
        //Sten Soomre Harjutus 2 Sten Soomre 24.01.2023
    $arv1 = 2;
    $arv2 = 4;
    $arv3 = 4.47;
    $vaste1 = $arv1 - $arv2;
    $vaste2 = $arv1 + $arv2;
    $vaste3 = $arv1 * $arv2;
    $vaste4 = $arv1 / $arv2;
    $vaste5 = $arv1 * 10;
    $vaste6 = $arv1 * 1000;
    $vaste7 = $arv1 * $arv2 / 2;
    $vaste8 = $arv1 + $arv2 + $arv3;
    echo "$arv1 - $arv2 = $vaste1 <br>";
    echo "$arv1 + $arv2 = $vaste2<br>";
    echo "$arv1 * $arv2 = $vaste3<br>";
    echo "$arv1 / $arv2 = $vaste4<br>";
    echo "<br><br>$arv1 cm = $vaste5 mm<br>$arv1 m = $vaste6 mm<br><br>";
    echo "Täisnurkse kolmnurga pindala, mille üks külg on $arv1 ja teine $arv2.<br>Selle pindala on S=a*b/2 ehk S=$arv1*$arv2/2<br>S=$vaste7<br>";
    echo "<br><br>Selle sama kolmnurga pindala oleks siis $arv1 + $arv2 + $arv3 = $vaste8";
    ?>
</body>
</html>