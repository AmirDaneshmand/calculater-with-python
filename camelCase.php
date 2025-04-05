<?php
$filename = "input.txt";
$content = file_get_contents($filename);


$line = trim($content);
$line = strtolower($line);
$formatted = ucwords($line); // بزرگ کردن حرف اول هر کلمه
$cleaned = str_replace(' ', '', $formatted);
$cleaned = lcfirst($cleaned);
echo $cleaned;

