<!DOCTYPE html>
<html>

<head>
  <title>Tervitus ja uudiskirja liitumine</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
    integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
    integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
    crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
    integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN"
    crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
    integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV"
    crossorigin="anonymous"></script>
</head>

<body>
  <div class="container">
    <h1 class="text-center">Tervitus ja uudiskirja liitumine</h1>
    <div class="alert alert-primary" role="alert">
      Tere päiksekesekene!
    </div>

    <form>
      <div class="form-group">
        <label for="username">Kasutajanimi</label>
        <input type="text" class="form-control" id="username" aria-describedby="usernameHelp">
        <small id="usernameHelp" class="form-text text-muted">Kasutajanimele luuakse " @hkhk.edu.ee " lõpuga
          email</small>
      </div>
      <div class="form-group">
        <label for="email">Emaili address</label>
        <input readonly type="email" class="form-control" id="email" aria-describedby="emailHelp">
        <small id="emailHelp" class="form-text text-muted">Me ei jaga teie emaili kellegagi.</small>
      </div>
      <div class="form-group">
        <label for="password">Salasõna</label>
        <input type="password" class="form-control" id="password">
      </div>
      <div class="form-group">

        <label for="code">Kood</label>
        <input readonly type="text" class="form-control" id="code" aria-describedby="codeHelp">
        <small id="codeHelp" class="form-text text-muted">Kood on 7-kohaline ja sisaldab tähti ja numbreid.</small>
      </div>
      <button type="submit" class="btn btn-primary">Liitu uudiskirjaga</button>
    </form>
    <script>

      //Kasutajanime
      function createUsername() {
        let username = document.getElementById("username").value;
        username = username.toLowerCase();
        document.getElementById("username").value = username;
      }

      //Email
      function createEmail() {
        let username = document.getElementById("username").value;
        let email = username + "@hkhk.edu.ee";
        document.getElementById("email").value = email;
      }

      //Kood
      function createCode() {
        let code = "";
        let possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        for (let i = 0; i < 7; i++) {
          code += possible.charAt(Math.floor(Math.random() * possible.length));
        }
        document.getElementById("code").value = code;
      }
      let form = document.querySelector("form");
      form.addEventListener("submit", function (event) {
        event.preventDefault();
        createUsername();
        createEmail();
        createCode();
      });
    </script>
    <div>
      <form action="" method="post">
        <div class="form-group">
          <label for="id_number">ID Number:</label>
          <input type="text" class="form-control" id="id_number" name="id_number" required>
        </div>
        <button type="submit" class="btn btn-primary">Check</button>
      </form>
      <?php
        //Sten Soomre Harjutus 7 Sten Soomre 01.03.2023
      if (isset($_POST["id_number"])) {
        $id_number = $_POST["id_number"];
        $id_length = strlen($id_number);
        if ($id_length != 11) {
          echo "<p class='mt-3'>ID number is not the right length</p>";
        } else {
          $gender = (int) substr($id_number, 0, 1) % 2 == 0 ? "female" : "male";
          $birth_year = (int) "" . substr($id_number, 2, 1);
          $birth_month = (int) substr($id_number, 3, 2);
          $birth_day = (int) substr($id_number, 5, 2);
          echo "<p class='mt-3'>The ID belongs to a " . $gender . " born on " . $birth_day . "." . $birth_month . "." . $birth_year . "</p>";
        }
      }
      ?>
    </div>
    <div>
      <form action="" method="post">
        <div class="form-group">
          <label for="start">Vahemiku algus:</label>
          <input type="number" class="form-control" id="start" name="start" required>
        </div>
        <div class="form-group">
          <label for="end">Vahemiku lõpp:</label>
          <input type="number" class="form-control" id="end" name="end" required>
        </div>
        <div class="form-group">
          <label for="step">Step:</label>
          <input type="number" class="form-control" id="step" name="step" value="1" required>
        </div>
        <button type="submit" class="btn btn-primary">Generate</button>
      </form>
      <?php
      if (isset($_POST["start"], $_POST["end"], $_POST["step"])) {
        $start = (int) $_POST["start"];
        $end = (int) $_POST["end"];
        $step = (int) $_POST["step"];
        echo "<ul class='mt-3'>";
        for ($i = $start; $i <= $end; $i += $step) {
          echo "<li>" . $i . "</li>";
        }
        echo "</ul>";

        $area = ($end - $start) / $step * $step;
        echo "<p class='mt-3'> ristkülikupindala on: " . $area . "</p>";
      }

      if (isset($_POST["start"], $_POST["end"], $_POST["step"])) {
        $start = (int) $_POST["start"];
        $end = (int) $_POST["end"];
        $step = (int) $_POST["step"];
        echo "<p class='mt-3'>";
        for ($i = $start; $i <= $end; $i += $step) {
          echo $i . " ";
        }
        echo "</p>";
      }
      ?>
    </div>
    <div class="container mt-5">
      <h1 class="text-center">Lause tegemine</h1>
      <p class="text-center">
        <?php
        // Define arrays
        $base = array("Ma", "Sina", "Tema", "Meie", "Teie", "Nad");
        $verb = array("olen", "oled", "on", "oleme", "olete", "on");
        $object = array("loom", "inimene", "loomariik", "riik", "maailm", "kodu");

        // Select random items from each array
        $random_base = $base[array_rand($base)];
        $random_verb = $verb[array_rand($verb)];
        $random_object = $object[array_rand($object)];

        // Combine the randomly selected items into a sentence
        $sentence = "$random_base $random_verb $random_object.";

        // Display the sentence
        echo $sentence;
        ?>
      </p>
    </div>
</body>

</html>