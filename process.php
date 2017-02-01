<?php 
$login = $_POST['login'];
$password = $_POST['password'];
$r = exec('python3 /home/bektemir/Рабочий\ стол/uber/server.py '.$login.' '.$password);
?>