$servers = @(
    "win-serv-1","win-serv-2",
    "win-serv-3","win-serv-4","win-serv-5",
    "win-serv-6","win-serv-7","win-serv-8",
    "win-serv-9","win-serv-10","win-serv-11","win-serv-12",
    "win-serv-13","win-serv-14","win-serv-15","win-serv-16",
    "win-serv-17","win-serv-18","win-serv-19","win-serv-20",
    "win-serv-21","win-serv-22","win-serv-23","win-serv-24"
)


$path = "D:\data\Depts"

$result = $servers | ForEach-Object {
    $server = $_
    Invoke-Command -ComputerName $server -ScriptBlock {
        param($p)

        $q = Get-FsrmQuota -Path $p
        $available = ($q.Size - $q.Usage) / 1GB

        [pscustomobject]@{
            Server    = $env:COMPUTERNAME
            AvailableGB = [math]::Round($available, 2)
        }
    } -ArgumentList $path
}

$result | ConvertTo-Json -Depth 3 -Compress
exit
