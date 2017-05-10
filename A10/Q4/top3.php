<?php
if (count($argv) != 2) {
	print "Usage: php top3.php <map_file>\n";
        print "e.g: php top3.php map.txt\n";
        exit();
}

$diff = array();

$map_file = fopen($argv[1], "r") or die("Unable to open map file!");

$counter = 0;
while(!feof($map_file)) {
	$raw_file_name = trim(fgets($map_file));
	if ($counter % 2 == 1) {
		$diff[$raw_file_name] = 0;
	}
	$counter++;
}

fclose($map_file);

foreach ($diff as $key => $value) {
	try {
		$old_file_path = "processedold/".$key; 
		$old_file_size = filesize($old_file_path);
		$new_file_path = "processednew/".$key;
		$new_file_size = filesize($new_file_path);
		$difference = abs($old_file_size - $new_file_size);
		$diff[$key] = $difference;
	} catch (Exception $e) {
		print $e->getMessage();
	}
} 

asort($diff);
 
$output_file = fopen("sizedifference.txt", "w") or die("Unable to create output file");
foreach ($diff as $key => $value) {
	$output = $key." --> ".$value."\n";
	fwrite($output_file, $output);
}
fclose($output_file);
?>
