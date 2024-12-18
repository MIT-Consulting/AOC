$lines = Get-Content input.txt
$left_nums = @()
$right_nums = @()

foreach ($line in $lines) {
    $nums = $line -split '\s+'
    $left_nums += [int]$nums[0]
    $right_nums += [int]$nums[1]
}

$left_nums = $left_nums | Sort-Object
$right_nums = $right_nums | Sort-Object

$total = 0
for ($i = 0; $i -lt $left_nums.Length; $i++) {
    $total += [Math]::Abs($left_nums[$i] - $right_nums[$i])
}

Write-Host "Total distance: $total" 