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
    <h1>Autosõiduaja Kalkulaator</h1>
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
          if ((strpos($aeg1, ":") !== false) or (strpos($aeg2, ":") !== false)) {
            if (strlen($aeg1) == 5) {
              if (strlen($aeg2) == 5) {
                $aeg1_parts = explode(':', $aeg1);
                $hours1 = substr($aeg1_parts[0], -2);
                $minutes1 = substr($aeg1_parts[1], 0, 2);
                $aeg2_parts = explode(':', $aeg2);
                $hours2 = substr($aeg2_parts[0], -2);
                $minutes2 = substr($aeg2_parts[1], 0, 2);
                $hours3 = $hours2 - $hours1;
                $minutes3 = $minutes2 - $minutes1;
                if ($hours3 < 0 or $minutes3 < 0) {
                  echo '<div class="alert alert-danger mt-4" role="alert">Lõppaeg ei saa olla pärast start aega!<br></div>';
                } else {
                  echo '<div class="alert alert-success mt-4" role="alert">Kulus ' . $hours3 . ' tundi ' . $minutes3 . ' minutit<br></div>';
                }
              } else {
                echo '<div class="alert alert-danger mt-4" role="alert">Lõpp aeg väli on vigane!<br></div>';
              }
            } else {
              echo '<div class="alert alert-danger mt-4" role="alert">Start aeg väli on vigane!<br></div>';
            }
          } else {
            echo '<div class="alert alert-danger mt-4" role="alert">Vigane vaste!<br></div>';
          }
        }

        ?>
      </div>
      <hr class= "mt-4">
      <h1>Diskrimatsiooni Kalkulaator</h1>
      <hr class= "mt-4">
      <div class="container">
        <?php
        $file = fopen("tootajad.csv", "r");
        $header = fgets($file);
        $male_salaries = [];
        $female_salaries = [];
        while (!feof($file)) {
            $line = fgets($file);
            $row = explode(";", $line);
            if (isset($row[1])) {
                if ($row[1] == "m") {
                    array_push($male_salaries, strval($row[2]));
                } else if ($row[1] == "n") {
                    array_push($female_salaries, strval($row[2]));
                }
            }
        }
        fclose($file);

        $male_average = array_sum($male_salaries) / count($male_salaries);
        $female_average = array_sum($female_salaries) / count($female_salaries);
        $male_highest = max($male_salaries);
        $female_highest = max($female_salaries);
        ?>
        <table class="table mt-5">
            <thead>
                <tr>
                    <th>Sugu</th>
                    <th>Keskmine palk</th>
                    <th>Kõrgem palk</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Mehed</td>
                    <td>
                        <?php echo "€" . number_format($male_average, 2); ?>
                    </td>
                    <td>
                        <?php echo "$" . $male_highest; ?>
                    </td>
                </tr>
                <tr>
                    <td>Naised</td>
                    <td>
                        <?php echo "€" . number_format($female_average, 2); ?>
                    </td>
                    <td>
                        <?php echo "€" . $female_highest; ?>
                    </td>
                </tr>
            </tbody>
        </table>
        <?php
        if ($male_average > $female_average) {
            echo '<div class="alert alert-danger mt-4" role="alert">Ettevõttes võib esineda soolist diskrimineerimist, kuna meeste keskmine palk on kõrgem kui naiste oma.</p>';
        } else if ($male_average < $female_average) {
            echo '<div class="alert alert-success mt-4" role="alert">Soolist diskrimineerimist ettevõttes ei esine, kuna naiste keskmine palk on meeste omaga kõrgem või võrdne.</p>';
        } else {
            echo '<div class="alert alert-success mt-4" role="alert">Soolist diskrimineerimist ettevõttes ei esine, kuna meeste ja naiste keskmine palk on võrdne.</div>';
        }
        ?>
    </div>
    </div>
</body>

</html>