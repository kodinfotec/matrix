# encoded by pyprotect
# http://live-tv.epizy.com/pyprotect

import base64, codecs
magic = 'IyBNb2R1bGU6IG1haW4KIyBBdXRob3I6IFJvbWFuIFYuIE0uCiMgQ3JlYXRlZCBvbjogMjguMTEuMjAxNAojIExpY2Vuc2U6IEdQTCB2LjMgaHR0cHM6Ly93d3cuZ251Lm9yZy9jb3B5bGVmdC9ncGwuaHRtbAoiIiIKRXhhbXBsZSB2aWRlbyBwbHVnaW4gdGhhdCBpcyBjb21wYXRpYmxlIHdpdGggS29kaSAxOS54ICJNYXRyaXgiIGFuZCBhYm92ZQoiIiIKaW1wb3J0IHN5cwpmcm9tIHVybGxpYi5wYXJzZSBpbXBvcnQgdXJsZW5jb2RlLCBwYXJzZV9xc2wKaW1wb3J0IHhibWNndWkKaW1wb3J0IHhibWNwbHVnaW4KCiMgR2V0IHRoZSBwbHVnaW4gdXJsIGluIHBsdWdpbjovLyBub3RhdGlvbi4KX1VSTCA9IHN5cy5hcmd2WzBdCiMgR2V0IHRoZSBwbHVnaW4gaGFuZGxlIGFzIGFuIGludGVnZXIgbnVtYmVyLgpfSEFORExFID0gaW50KHN5cy5hcmd2WzFdKQoKIyBGcmVlIHNhbXBsZSB2aWRlb3MgYXJlIHByb3ZpZGVkIGJ5IHd3dy52aWRzcGxheS5jb20KIyBIZXJlIHdlIHVzZSBhIGZpeGVkIHNldCBvZiBwcm9wZXJ0aWVzIHNpbXBseSBmb3IgZGVtb25zdHJhdGluZyBwdXJwb3NlcwojIEluIGEgInJlYWwgbGlmZSIgcGx1Z2luIHlvdSB3aWxsIG5lZWQgdG8gZ2V0IGluZm8gYW5kIGxpbmtzIHRvIHZpZGVvIGZpbGVzL3N0cmVhbXMKIyBmcm9tIHNvbWUgd2ViLXNpdGUgb3Igb25saW5lIHNlcnZpY2UuClZJREVPUyA9IHsnW0JdSEJPW0NPTE9SIG9yYW5nZV1NQVhbL0NPTE9SXSBbL0JdJzogW3snbmFtZSc6ICdbQl1IQk9bQ09MT1Igb3JhbmdlXU1BWFsvQ09MT1JdIFsvQl0nLAogICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdodHRwczovL2kuaW1ndXIuY29tL1FDdW45aGQucG5nJywKICAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAnUk4nLAogICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQl0gW0NPTE9SIG9yYW5nZV1GSUxNRVNbL0NPTE9SXSBIQk9bQ09MT1Igb3JhbmdlXU1BWFsvQ09MT1JdWy9CXSBbIEJ5IC0gSW5mb3RlYy1Lb2RpLU9ubGluZS1NYXRyaXggXSd9LAogICAgICAgICAgICAgICAgICAgICAgIHsnbmFtZSc6ICdORU0gVU0gUEFTU08gRU0gRkFMU08gW0NPTE9SIG9yYW5nZV1UTURiOiA3MCUgW0NPTE9SIGxpbWVdMjAyMVsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsL29odVFpY1c4MTg4dVprYXpVWVp3SGVmR05xZC5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6YjJkMzAyY2Q1ZjA4YzRlODUzOWNlMmEzZDFjYTcyNjljMmM3NGMxNCcsCiAgICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDI0LzA2LzIwMjEgKERFKSB8IENyaW1lLCBEcmFtYSwgVGhyaWxsZXIsIE1pc3TDqXJpbyB8IDFoIDU1bSBbL0NPTE9SXSd9LAogICAgICAgICAgICAgICAgICAgICAgIHsnbmFtZSc6ICfDgFMgQ0VHQVMgW0NPTE9SIG9yYW5nZV1UTURiOiA3OCUgW0NPTE9SIGxpbWVdMjAyMFsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsL3VCaTVDRjdGanNVNWdFTDdsbVB2b2kxNUEwTy5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6MGI1NDcxMzY2OTY2ZGZiMGFlMDc0NTM4OTYzMTQ5MjJkYmRhOWIwZicsCiAgICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDE0LzEyLzIwMjAgKEJSKSB8IFRocmlsbGVyIHwgMWggMjltIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ0EgSUxIQSBEQSBGQU5UQVNJQSBbQ09MT1Igb3JhbmdlXVRNRGI6IDYxJSBbQ09MT1IgbGltZV0yMDIwWy9DT0xPUl0nLAogICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdodHRwczovL3d3dy50aGVtb3ZpZWRiLm9yZy90L3Avb3JpZ2luYWwvZWVCWmVmbTNucmpLNUxnNFRQcm9PUXJ0ZFRMLmpwZycsCiAgICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ3BsdWdpbjovL3BsdWdpbi52aWRlby5lbGVtZW50dW0vcGxheT91cmk9bWFnbmV0Oj94dD11cm46YnRpaDowNzQ0ZWQwZjdjNDE3Y2Y0ZTliYjMzMGVlY2YyODNkNzYyOTE3YTFjJywKICAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMDkvMDQvMjAyMCAoQlIpIHwgVGVycm9yLCBGYW50YXNpYSwgQXZlbnR1cmEsIE1pc3TDqXJpbyB8IDFoIDUwbSBbL0NPTE9SXSd9LAogICAgICAgICAgICAgICAgICAgICAgIHsnbmFtZSc6ICdBVkVTIERFIFJBUElOQSBbQ09MT1Igb3JhbmdlXVRNRGI6IDcxJSBbQ09MT1IgbGltZV0yMDIwWy9DT0xPUl0nLAogICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdodHRwczovL3d3dy50aGVtb3ZpZWRiLm9yZy90L3Avb3JpZ2luYWwvYUxFSnRrYWhqaE1YNlJnMWtJSkpqb3hhWVdZLmpwZycsCiAgICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ3BsdWdpbjovL3BsdWdpbi52aWRlby5lbGVtZW50dW0vcGxheT91cmk9bWFnbmV0Oj94dD11cm46YnRpaDo5MDg1Q0I0MDFENUZCOUM1RTM3QjhFMkFFNDExRUZFOURFQzI3NDk1JywKICAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMDYvMDIvMjAyMCAoQlIpIHwgQcOnw6NvLCBDcmltZSB8IDFoIDQ5bSBbL0NPTE9SXSd9LCAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ0FOTkFCRUxMRTogMyBbQ09MT1Igb3JhbmdlXVRNRGI6IDcxJSBbQ09MT1IgbGltZV0yMDE5Wy9DT0xPUl0nLAogICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdodHRwczovL3d3dy50aGVtb3ZpZWRiLm9yZy90L3Avb3JpZ2luYWwvd0xtSGZndEJQcjEzMVlDM29pdjRjMFpjdEZuLmpwZycsCiAgICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ3BsdWdpbjovL3BsdWdpbi52aWRlby5lbGVtZW50dW0vcGxheT91cmk9bWFnbmV0Oj94dD11cm46YnRpaDo5MTRDMTk0RUREQkY3NjRDOTQ5RDEzNkM5Rjc5RTdFNEI2MEJCNDQyJywKICAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMjcvMDYvMjAxOSAoQlIpIHwgVGVycm9yLCBUaHJpbGxlciwgTWlzdMOpcmlvIHwgMWggNDZtIFsvQ09MT1JdJ30sICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnQkFEIEJPWVM6IFBBUkEgU0VNUFJFIFtDT0xPUiBvcmFuZ2VdVE1EYjogNzMlIFtDT0xPUiBsaW1lXTIwMjBbL0NPTE9SXScsCiAgICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vd3d3LnRoZW1vdmllZGIub3JnL3QvcC9vcmlnaW5hbC92WTVCSnEzeDhKMFVSNHVySWRFbmdIc0tBYk8uanBnJywKICAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLmVsZW1lbnR1bS9wbGF5P3VyaT1tYWduZXQ6P3h0PXVybjpidGloOjVkZWU2N2I4NTU3ZWViOWI0ZTRlZmFkYTk0ZDk2YjgxZjBlNjllZTUnLAogICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQ09MT1Igb3JhbmdlXSAzMC8wMS8yMDIwIChCUikgfCBUaHJpbGxlciwgQcOnw6NvLCBDcmltZSB8IDFoIDUzbSBbL0NPTE9SXSd9LCAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ09TIFBFUVVFTk9TIFZFU1TDjUdJT1MgW0NPTE9SIG9yYW5nZV1UTURiOiA3MSUgW0NPTE9SIGxpbWVdMjAyMVsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsLzM1OUw2U1FkNTJHdlRwb3lWU0VRdURRNU9BQy5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uc21yX2xpbmtfdGVzdGVyLz9tb2RlPXBsYXlfbGluayZhbXA7bGluaz1odHRwczovL3Vwc3RyZWFtLnRvL3Z6NXlvYTlpN2UxbScsCiAgICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDI4LzAxLzIwMjEgKEJSKSBUaHJpbGxlciwgQ3JpbWUgWy9DT0xPUl0nfSwKICAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnQSBFU0NBVkHDh8ODTyBbQ09MT1Igb3JhbmdlXVRNRGI6IDc1JSBbQ09MT1IgbGltZV0yMDIxWy9DT0xPUl0nLAogICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdodHRwczovL3d3dy50aGVtb3ZpZWRiLm9yZy90L3Avb3JpZ2luYWwvNGMwVDg4RTFzYnVsTnloRWEybkVsbU85YWE3LmpwZycsCiAgICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ3BsdWdpbjovL3BsdWdpbi52aWRlby5lbGVtZW50dW0vcGxheT91cmk9bWFnbmV0Oj94dD11cm46YnRpaDpjZjJmMWM3Yzc4NDM2NWE1ZjhmYzZjZmIwZTM2NDEyZTY1NjBiZGVmJmRuPUNPTU9FVUJBSVhPLkNPTS4uV0VCLURMLk1LVi5DT01BTkRPLlRPJTIwLSUyMEElMjBFc2NhdmElYzMlYTclYzMlYTNvJTIwMjAyMSUyMDEwODBwJTIwNS4xJTIwRFVBTCZ0cj11ZHAlM2ElMmYlMmZ0cmFja2VyLm9wZW5iaXR0b3JyZW50LmNvbSUzYTgwJTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmdHJhY2tlci5vcGVudHJhY2tyLm9yZyUzYTEzMzclMmZhbm5vdW5jZSZ0cj11ZHAlM2ElMmYlMmZ0cmFja2VyLmNvcHBlcnN1cmZlci50ayUzYTY5NjklMmZhbm5vdW5jZSZ0cj11ZHAlM2ElMmYlMmZnbG90b3JyZW50cy5wdyUzYTY5NjklMmZhbm5vdW5jZSZ0cj11ZHAlM2ElMmYlMmZ0cmFja2VyNC5waXJhdHV4LmNvbSUzYTY5NjklMmZhbm5vdW5jZSZ0cj11ZHAlM2ElMmYlMmZjb3BwZXJzdXJmZXIudGslM2E2OTY5JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmcmV0cmFja2VyLmxhbnRhLW5ldC5ydSUzYTI3MTAlMmZhbm5vdW5jZSZ0cj11ZHAlM2ElMmYlMmZ0cmFja2VyLnRpbnktdnBzLmNvbSUzYTY5NjklMmZhbm5vdW5jZSZ0cj11ZHAlM2ElMmYlMmZvcGVuLnN0ZWFsdGguc2klM2E4MCUyZmFubm91bmNlJnRyPXVkcCUzYSUyZiUyZmV4b2R1cy5kZXN5bmMuY29tJTNhNjk2OSUyZmFubm91bmNlJnRyPWh0dHAlM2ElMmYlMmZ0cmFja2VyLmNvcHBlcnN1cmZlci50ayUzYTY5NjklMmZhbm5vdW5jZSZ0cj1odHRwJTNhJTJmJTJmYnQuY2FyZWxhbmQuY29tLmNuJTNhNjk2OSUyZmFubm91bmNlJnRyPWh0dHAlM2ElMmYlMmZleG9kdXMuZGVzeW5jLmNvbSUzYTY5NjklMmZhbm5vdW5jZSZ0cj11ZHAlM2ElMmYlMmZ0cmFja2VyLmN5YmVyaWEuaXMlM2E2OTY5JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmcHVibGljLnBvcGNvcm4tdHJhY2tlci5vcmc'
love = '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'
god = 'kwOTBkOGU4Y2NjN2QxNTU2YycsCiAgICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDI4LzA3LzIwMjAgKFVTKSB8IEHDp8OjbywgVGVycm9yLCBGaWPDp8OjbyBjaWVudMOtZmljYSB8IDFoIDQwbSBbL0NPTE9SXSd9LAogICAgICAgICAgICAgICAgICAgICAgIHsnbmFtZSc6ICdOTyBPTEhPIERPIFRPUk5BRE8gW0NPTE9SIG9yYW5nZV1UTURiOiA2MCUgW0NPTE9SIGxpbWVdMjAxNFsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsL0FtUExmdkNjOUxHeW85bVJMcEljRTRzNmNsTi5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6OGIyZWQ1ZWFkNjliYjc0ZmFhNDc5OTQzMmRjMTFhZTNkMmQ5Y2Y1NScsCiAgICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDI3LzA4LzIwMTQgKEJSKSB8IEHDp8OjbywgVGhyaWxsZXIgfCAxaCAyOW0gWy9DT0xPUl0nfSwKICAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnTyBNRU5TQUdFSVJPIFtDT0xPUiBvcmFuZ2VdVE1EYjogNzAlIFtDT0xPUiBsaW1lXTE5OTdbL0NPTE9SXScsCiAgICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vd3d3LnRoZW1vdmllZGIub3JnL3QvcC9vcmlnaW5hbC81bnpHTnNOQzh6UXNzVkF3NlNMOHdIbDE2N2IuanBnJywKICAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLmVsZW1lbnR1bS9wbGF5P3VyaT1tYWduZXQ6P3h0PXVybjpidGloOmU3NGU3YWNiODNjODI4NmY0NWIwOWU3NzA1ZGJkZWRkYThjYjljY2QnLAogICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQ09MT1Igb3JhbmdlXSAyNS8xMi8xOTk3IChVUykgfCBGaWPDp8OjbyBjaWVudMOtZmljYSwgQXZlbnR1cmEsIEHDp8OjbywgR3VlcnJhIHwgMmggNTdtIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ08gQ0FNSU5ITyBERSBWT0xUQSBbQ09MT1Igb3JhbmdlXVRNRGI6IDY3JSBbQ09MT1IgbGltZV0yMDIwWy9DT0xPUl0nLAogICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdodHRwczovL3d3dy50aGVtb3ZpZWRiLm9yZy90L3Avb3JpZ2luYWwvb3Y1YVVDSWhqMEtON3FQUWY5TXZualVGdmZ5LmpwZycsCiAgICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ3BsdWdpbjovL3BsdWdpbi52aWRlby5lbGVtZW50dW0vcGxheT91cmk9bWFnbmV0Oj94dD11cm46YnRpaDplNGM5ZDZkYTk0MDkyMjVkYzE0MmQ0MjZiYTFkNmQxZGJiMmIxZmI1JywKICAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMjMvMDQvMjAyMCAoQlIpIHwgRHJhbWEgfCAxaCA0OG0gWy9DT0xPUl0nfSwKICAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnTyBBVElSQURPUjogTyBGSU0gREUgVU0gQVNTQVNTSU5PIFtDT0xPUiBvcmFuZ2VdVE1EYjogNjUlIFtDT0xPUiBsaW1lXTIwMjBbL0NPTE9SXScsCiAgICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vd3d3LnRoZW1vdmllZGIub3JnL3QvcC9vcmlnaW5hbC9mdTBIeUZCMWIyUmwxNzdrcDVYUGxEU2taRmkuanBnJywKICAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLmVsZW1lbnR1bS9wbGF5P3VyaT1tYWduZXQ6P3h0PXVybjpidGloOllLNDRNWkw3SldFTzNLTEU0UUFLVUM3SjQzNTJHUjVWJywKICAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMTYvMDYvMjAyMCAoVVMpIHwgQcOnw6NvIHwgMWggMzBtIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ08gR1JJVE8gW0NPTE9SIG9yYW5nZV1UTURiOiA2NyUgW0NPTE9SIGxpbWVdMjAyMFsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsL283Sk1tQURoWlNIVGJQb2xiTEttSkEydXIwdC5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6YzdjZGZhMzA4YzU5OWIxM2UyZDY3OGM0YmNjOGRlNDZmOTMzNmUxMScsCiAgICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDEzLzAyLzIwMjAgKEJSKSB8IFRlcnJvciwgTWlzdMOpcmlvIHwgMWggMzNtIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ08gQ0hBTMOJIFtDT0xPUiBvcmFuZ2VdVE1EYjogNjUlIFtDT0xPUiBsaW1lXTIwMjBbL0NPTE9SXScsCiAgICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vd3d3LnRoZW1vdmllZGIub3JnL3QvcC9vcmlnaW5hbC9BNUxldmRqU0lRMTJOYzMwdVVabk9ta2UyYk8uanBnJywKICAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLmVsZW1lbnR1bS9wbGF5P3VyaT1tYWduZXQ6P3h0PXVybjpidGloOjg3OTQxYTQxYjhmM2ZkODA2MjE5MDM1Zjc2YzY4MGI1YWNjODcwNzUnLAogICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQ09MT1Igb3JhbmdlXSAwNi8wMi8yMDIwIChCUikgfCBEcmFtYSwgVGVycm9yLCBUaHJpbGxlciB8IDFoIDQ4bSBbL0NPTE9SXSd9LAogICAgICAgICAgICAgICAgICAgICAgIHsnbmFtZSc6ICdTRU0gUkVUT1JOTyBbQ09MT1Igb3JhbmdlXVRNRGI6IDY5JSBbQ09MT1IgbGltZV0yMDE1Wy9DT0xPUl0nLAogICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdodHRwczovL3d3dy50aGVtb3ZpZWRiLm9yZy90L3Avb3JpZ2luYWwvaEptbUpRMGVGQW10YlRFUlloekpabWhYdE12LmpwZycsCiAgICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ3BsdWdpbjovL3BsdWdpbi52aWRlby5lbGVtZW50dW0vcGxheT91cmk9bWFnbmV0Oj94dD11cm46YnRpaDpCMUY4QUQwNDZDQjUwN0M5RkZCNjMyNkVEMjk5QkY1OTM2QjQ5OUQzJywKICAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMDEvMTIvMjAxNSAoQlIpIHwgRmljw6fDo28gY2llbnTDrWZpY2EsIE1pc3TDqXJpbywgVGhyaWxsZXIgfCAxaCA1OG0gWy9DT0xPUl0nfQogICAgICAgICAgICAgICAgICAgICBdfQpkZWYgZ2V0X3VybCgqKmt3YXJncyk6CiAgICAiIiIKICAgIENyZWF0ZSBhIFVSTCBmb3IgY2FsbGluZyB0aGUgcGx1Z2luIHJlY3Vyc2l2ZWx5IGZyb20gdGhlIGdpdmVuIHNldCBvZiBrZXl3b3JkIGFyZ3VtZW50cy4KCiAgICA6cGFyYW0ga3dhcmdzOiAiYXJndW1lbnQ9dmFsdWUiIHBhaXJzCiAgICA6cmV0dXJuOiBwbHVnaW4gY2FsbCBVUkwKICAgIDpydHlwZTogc3RyCiAgICAiIiIKICAgIHJldHVybiAne30/e30nLmZvcm1hdChfVVJMLCB1cmxlbmNvZGUoa3dhcmdzKSkKCgpkZWYgZ2V0X2NhdGVnb3JpZXMoKToKICAgICIiIgogICAgR2V0IHRoZSBsaXN0IG9mIHZpZGVvIGNhdGVnb3JpZXMuCgogICAgSGVyZSB5b3UgY2FuIGluc2VydCBzb21lIHBhcnNpbmcgY29kZSB0aGF0IHJldHJpZXZlcwogICAgdGhlIGxpc3Qgb2YgdmlkZW8gY2F0ZWdvcmllcyAoZS5nLiAnTW92aWVzJywgJ1RWLXNob3dzJywgJ0RvY3VtZW50YXJpZXMnIGV0Yy4pCiAgICBmcm9tIHNvbWUgc2l0ZSBvciBBUEkuCgogICAgLi4gbm90ZTo6IENvbnNpZGVyIHVzaW5nIGBnZW5lcmF0b3IgZnVuY3Rpb25zIDxodHRwczovL3dpa2kucHl0aG9uLm9yZy9tb2luL0dlbmVyYXRvcnM+YF8KICAgICAgICBpbnN0ZWFkIG9mIHJldHVybmluZyBsaXN0cy4KCiAgICA6cmV0dXJuOiBUaGUgbGlzdCBvZiB2aWRlbyBjYXRlZ29yaWVzCiAgICA6cnR5cGU6IHR5cGVzLkdlbmVyYXRvclR5cGUKICAgICIiIgogICAgcmV0dXJuIFZJREVPUy5rZXlzKCkKCgpkZWYgZ2V0X3ZpZGVvcyhjYXRlZ29yeSk6CiAgICAiIiIKICAgIEdldCB0aGUgbGlzdCBvZiB2aWRlb2ZpbGVzL3N0cmVhbXMuCgogICAgSGVyZSB5b3UgY2FuIGluc2VydCBzb21lIHBhcnNpbmcgY29kZSB0aGF0IHJldHJpZXZlcwogICAgdGhlIGxpc3Qgb2YgdmlkZW8gc3RyZWFtcyBpbiB0aGUgZ2l2ZW4gY2F0ZWdvcnkgZnJvbSBzb21lIHNpdGUgb3IgQVBJLgoKICAgIC4uIG5vdGU6OiBDb25zaWRlciB1c2luZyBgZ2VuZXJhdG9ycyBmdW5jdGlvbnMgPGh0dHBzOi8vd2lraS5weXRob24ub3JnL21vaW4vR2VuZXJhdG9ycz5gXwogICAgICAgIGluc3RlYWQgb2YgcmV0dXJuaW5nIGxpc3RzLgoKICAgIDpwYXJhbSBjYXRlZ29yeTogQ2F0ZWdvcnkgbmFtZQogICAgOnR5cGUgY2F0ZWdvcnk6IHN0cgogICAgOnJldHVybjogdGhlIGxpc3Qgb2YgdmlkZW9zIGluIHRoZSBjYXRlZ29yeQogICAgOnJ0eXBlOiBsaXN0CiAgICAiIiIKICAgIHJldHVybiBWSURFT1NbY2F0ZWdvcnldCgoKZGVmIGxpc3RfY2F0ZWdvcmllcygpOgogICAgIiIiCiAgICBDcmVhdGUgdGhlIGxpc3Qgb2YgdmlkZW8gY2F0ZWdvcmllcyBpbiB0aGUgS29kaSBpbnRlcmZhY2UuCiAgICAiIiIKICAgICMgU2V0IHBsdWdpbiBjYXRlZ29yeS4gSXQgaXMgZGlzcGxheWVkIGluIHNvbWUgc2tpbnMgYXMgdGhlIG5hbWUKICAgICMgb2YgdGhlIGN1cnJlbnQgc2VjdGlvbi4KICAgIHhibWNwbHVnaW4uc2V0UGx1Z2luQ2F0ZWdvcnkoX0hBTkRMRSwgJ015IFZpZGVvIENvbGxlY3Rpb24nKQogICAgIyBTZXQgcGx1Z2luIGNvbnRlbnQuIEl0IGFsbG93cyBLb2RpIHRvIHNlbGVjdCBhcHByb3ByaWF0ZSB2aWV3cwogICAgIyBmb3IgdGhpcyB0eXBlIG9mIGNvbnRlbnQuCiAgICB4Ym1jcGx1Z2luLnNldENvbnRlbnQoX0hBTkRMRSwgJ3ZpZGVvcycpCiAgICAjIEdldCB2aWRlbyBjYXRlZ29yaWVzCiAgICBjYXRlZ29yaWVzID0gZ2V0X2NhdGVnb3JpZXMoKQogICAgIyBJdGVyYXRlIHRocm91Z2ggY2F0ZWdvcmllcwogICAgZm9yIGNhdGVnb3J5IGluIGNhdGVnb3JpZXM6CiAgICAgICAgIyBDcmVhdGUgYSBsaXN0IGl0ZW0gd2l0aCBhIHRleHQgbGFiZWwgYW5kIGEgdGh1bWJuYWlsIGltYWdlLgogICAgICAgIGxpc3RfaXRlbSA9IHhibWNndWkuTGlzdEl0ZW0obGFiZWw9Y2F0ZWdvcnkpCiAgICAgICAgIyBTZXQgZ3JhcGhpY3MgKHRodW1ibmFpbCwgZmFuYXJ0LCBiYW5uZXIsIHBvc3RlciwgbGFuZHNjYXBlIGV0Yy4pIGZvciB0aGUgbGlzdCBpdGVtLgogICAgICAgICMgSGVyZSB3ZSB1c2UgdGhlIHNhbWUgaW1hZ2UgZm9yIGFsbCBpdGVtcyBmb3Igc2ltcGxpY2l0eSdzIHNha2UuCiAgICAgICAgIyBJbiBhIHJlYWwtbGlmZSBwbHVnaW4geW91IG5lZWQgdG8gc2V0IGVhY2ggaW1hZ2UgYWNjb3JkaW5nbHkuCiAgI'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))