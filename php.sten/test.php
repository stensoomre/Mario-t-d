<?php
$dir = "./";

// Avame kataloogi
$dh = opendir($dir);

// Loeme kataloogist failide nimekirja
while (($file = readdir($dh)) !== false) {
  // Kontrollime, kas fail on .php laiendiga
  if (pathinfo($file, PATHINFO_EXTENSION) == "php") {
    // Loome lingi failile
    echo "<a href='$file'>$file</a><br>";
  }
}

// Sulgeme kataloogi
closedir($dh);
?>
