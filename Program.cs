using System.Diagnostics;
using System.Reflection;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

var appVersion = Assembly.GetExecutingAssembly()
    .GetCustomAttribute<AssemblyInformationalVersionAttribute>()?
    .InformationalVersion.Split('+')[0] ?? "unknown";
var commitVersion = await GetCommitVersionAsync(app.Environment.ContentRootPath);

app.MapGet("/", () => Results.File(
    Path.Combine(app.Environment.ContentRootPath, "index.html"),
    "text/html; charset=utf-8"));
app.MapGet("/cat.jpg", () => Results.File(
    Path.Combine(app.Environment.ContentRootPath, "cat.jpg"),
    "image/jpeg"));
app.MapGet("/api/version", () => Results.Ok(new
{
    version = appVersion,
    commit = commitVersion
}));

app.Run();

static async Task<string> GetCommitVersionAsync(string workingDirectory)
{
    try
    {
        using var process = Process.Start(new ProcessStartInfo
        {
            FileName = "git",
            Arguments = "rev-parse --short HEAD",
            WorkingDirectory = workingDirectory,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true
        });

        if (process is null)
        {
            return "unavailable";
        }

        var output = await process.StandardOutput.ReadToEndAsync();
        await process.WaitForExitAsync();
        return process.ExitCode == 0 ? output.Trim() : "unavailable";
    }
    catch
    {
        return "unavailable";
    }
}
