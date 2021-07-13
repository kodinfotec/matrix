# encoded by pyprotect
# http://live-tv.epizy.com/pyprotect

import base64, codecs
magic = 'IyBNb2R1bGU6IG1haW4KIyBBdXRob3I6IFJvbWFuIFYuIE0uCiMgQ3JlYXRlZCBvbjogMjguMTEuMjAxNAojIExpY2Vuc2U6IEdQTCB2LjMgaHR0cHM6Ly93d3cuZ251Lm9yZy9jb3B5bGVmdC9ncGwuaHRtbAoiIiIKRXhhbXBsZSB2aWRlbyBwbHVnaW4gdGhhdCBpcyBjb21wYXRpYmxlIHdpdGggS29kaSAxOS54ICJNYXRyaXgiIGFuZCBhYm92ZQoiIiIKaW1wb3J0IHN5cwpmcm9tIHVybGxpYi5wYXJzZSBpbXBvcnQgdXJsZW5jb2RlLCBwYXJzZV9xc2wKaW1wb3J0IHhibWNndWkKaW1wb3J0IHhibWNwbHVnaW4KCiMgR2V0IHRoZSBwbHVnaW4gdXJsIGluIHBsdWdpbjovLyBub3RhdGlvbi4KX1VSTCA9IHN5cy5hcmd2WzBdCiMgR2V0IHRoZSBwbHVnaW4gaGFuZGxlIGFzIGFuIGludGVnZXIgbnVtYmVyLgpfSEFORExFID0gaW50KHN5cy5hcmd2WzFdKQoKIyBGcmVlIHNhbXBsZSB2aWRlb3MgYXJlIHByb3ZpZGVkIGJ5IHd3dy52aWRzcGxheS5jb20KIyBIZXJlIHdlIHVzZSBhIGZpeGVkIHNldCBvZiBwcm9wZXJ0aWVzIHNpbXBseSBmb3IgZGVtb25zdHJhdGluZyBwdXJwb3NlcwojIEluIGEgInJlYWwgbGlmZSIgcGx1Z2luIHlvdSB3aWxsIG5lZWQgdG8gZ2V0IGluZm8gYW5kIGxpbmtzIHRvIHZpZGVvIGZpbGVzL3N0cmVhbXMKIyBmcm9tIHNvbWUgd2ViLXNpdGUgb3Igb25saW5lIHNlcnZpY2UuClZJREVPUyA9IHsnW0JdSEJPW0NPTE9SIG9yYW5nZV1NQVhbL0NPTE9SXSBbL0JdJzogW3snbmFtZSc6ICdbQl1IQk9bQ09MT1Igb3JhbmdlXU1BWFsvQ09MT1JdIFsvQl0nLAogICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdodHRwczovL2kuaW1ndXIuY29tL1FDdW45aGQucG5nJywKICAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAnUk4nLAogICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQl0gW0NPTE9SIG9yYW5nZV1GSUxNRVNbL0NPTE9SXSBIQk9bQ09MT1Igb3JhbmdlXU1BWFsvQ09MT1JdWy9CXSBbIEJ5IC0gW0NPTE9SIG9yYW5nZV1JbmZvdGVjLUtvZGktT25saW5lLU1hdHJpeFsvQ09MT1JdIF0gUElYIFtDT0xPUiBvcmFuZ2VdIGVzcGVjaWFsY3NAbGl2ZS5jb20gWy9DT0xPUl0nfSwKICAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnTkVNIFVNIFBBU1NPIEVNIEZBTFNPIFtDT0xPUiBvcmFuZ2VdVE1EYjogNzAlIFtDT0xPUiBsaW1lXTIwMjFbL0NPTE9SXScsCiAgICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vd3d3LnRoZW1vdmllZGIub3JnL3QvcC9vcmlnaW5hbC9vaHVRaWNXODE4OHVaa2F6VVlad0hlZkdOcWQuanBnJywKICAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLmVsZW1lbnR1bS9wbGF5P3VyaT1tYWduZXQ6P3h0PXVybjpidGloOmIyZDMwMmNkNWYwOGM0ZTg1MzljZTJhM2QxY2E3MjY5YzJjNzRjMTQnLAogICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQ09MT1Igb3JhbmdlXSAyNC8wNi8yMDIxIChERSkgfCBDcmltZSwgRHJhbWEsIFRocmlsbGVyLCBNaXN0w6lyaW8gfCAxaCA1NW0gWy9DT0xPUl0nfSwKICAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnw4BTIENFR0FTIFtDT0xPUiBvcmFuZ2VdVE1EYjogNzglIFtDT0xPUiBsaW1lXTIwMjBbL0NPTE9SXScsCiAgICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vd3d3LnRoZW1vdmllZGIub3JnL3QvcC9vcmlnaW5hbC91Qmk1Q0Y3RmpzVTVnRUw3bG1Qdm9pMTVBME8uanBnJywKICAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLmVsZW1lbnR1bS9wbGF5P3VyaT1tYWduZXQ6P3h0PXVybjpidGloOjBiNTQ3MTM2Njk2NmRmYjBhZTA3NDUzODk2MzE0OTIyZGJkYTliMGYnLAogICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQ09MT1Igb3JhbmdlXSAxNC8xMi8yMDIwIChCUikgfCBUaHJpbGxlciB8IDFoIDI5bSBbL0NPTE9SXSd9LAogICAgICAgICAgICAgICAgICAgICAgIHsnbmFtZSc6ICdBIElMSEEgREEgRkFOVEFTSUEgW0NPTE9SIG9yYW5nZV1UTURiOiA2MSUgW0NPTE9SIGxpbWVdMjAyMFsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsL2VlQlplZm0zbnJqSzVMZzRUUHJvT1FydGRUTC5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6MDc0NGVkMGY3YzQxN2NmNGU5YmIzMzBlZWNmMjgzZDc2MjkxN2ExYycsCiAgICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDA5LzA0LzIwMjAgKEJSKSB8IFRlcnJvciwgRmFudGFzaWEsIEF2ZW50dXJhLCBNaXN0w6lyaW8gfCAxaCA1MG0gWy9DT0xPUl0nfSwKICAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnQVZFUyBERSBSQVBJTkEgW0NPTE9SIG9yYW5nZV1UTURiOiA3MSUgW0NPTE9SIGxpbWVdMjAyMFsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsL2FMRUp0a2FoamhNWDZSZzFrSUpKam94YVlXWS5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6OTA4NUNCNDAxRDVGQjlDNUUzN0I4RTJBRTQxMUVGRTlERUMyNzQ5NScsCiAgICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDA2LzAyLzIwMjAgKEJSKSB8IEHDp8OjbywgQ3JpbWUgfCAxaCA0OW0gWy9DT0xPUl0nfSwgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgIHsnbmFtZSc6ICdBTk5BQkVMTEU6IDMgW0NPTE9SIG9yYW5nZV1UTURiOiA3MSUgW0NPTE9SIGxpbWVdMjAxOVsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsL3dMbUhmZ3RCUHIxMzFZQzNvaXY0YzBaY3RGbi5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6OTE0QzE5NEVEREJGNzY0Qzk0OUQxMzZDOUY3OUU3RTRCNjBCQjQ0MicsCiAgICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDI3LzA2LzIwMTkgKEJSKSB8IFRlcnJvciwgVGhyaWxsZXIsIE1pc3TDqXJpbyB8IDFoIDQ2bSBbL0NPTE9SXSd9LCAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ0JBRCBCT1lTOiBQQVJBIFNFTVBSRSBbQ09MT1Igb3JhbmdlXVRNRGI6IDczJSBbQ09MT1IgbGltZV0yMDIwWy9DT0xPUl0nLAogICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdodHRwczovL3d3dy50aGVtb3ZpZWRiLm9yZy90L3Avb3JpZ2luYWwvdlk1QkpxM3g4SjBVUjR1cklkRW5nSHNLQWJPLmpwZycsCiAgICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ3BsdWdpbjovL3BsdWdpbi52aWRlby5lbGVtZW50dW0vcGxheT91cmk9bWFnbmV0Oj94dD11cm46YnRpaDo1ZGVlNjdiODU1N2VlYjliNGU0ZWZhZGE5NGQ5NmI4MWYwZTY5ZWU1JywKICAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMzAvMDEvMjAyMCAoQlIpIHwgVGhyaWxsZXIsIEHDp8OjbywgQ3JpbWUgfCAxaCA1M20gWy9DT0xPUl0nfSwgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgIHsnbmFtZSc6ICdPUyBQRVFVRU5PUyBWRVNUw41HSU9TIFtDT0xPUiBvcmFuZ2VdVE1EYjogNzElIFtDT0xPUiBsaW1lXTIwMjFbL0NPTE9SXScsCiAgICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vd3d3LnRoZW1vdmllZGIub3JnL3QvcC9vcmlnaW5hbC8zNTlMNlNRZDUyR3ZUcG95VlNFUXVEUTVPQUMuanBnJywKICAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLnNtcl9saW5rX3Rlc3Rlci8/bW9kZT1wbGF5X2xpbmsmYW1wO2xpbms9aHR0cHM6Ly91cHN0cmVhbS50by92ejV5b2E5aTdlMW0nLAogICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQ09MT1Igb3JhbmdlXSAyOC8wMS8yMDIxIChCUikgVGhyaWxsZXIsIENyaW1lIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ0EgRVNDQVZBw4fDg08gW0NPTE9SIG9yYW5nZV1UTURiOiA3NSUgW0NPTE9SIGxpbWVdMjAyMVsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsLzRjMFQ4OEUxc2J1bE55aEVhMm5FbG1POWFhNy5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6Y2YyZjFjN2M3ODQzNjVhNWY4ZmM2Y2ZiMGUzNjQxMmU2NTYwYmRlZiZkbj1DT01PRVVCQUlYTy5DT00uLldFQi1ETC5NS1YuQ09NQU5ETy5UTyUyMC0lMjBBJTIwRXNjYXZhJWMzJWE3JWMzJWEzbyUyMDIwMjElMjAxMDgwcCUyMDUuMSUyMERVQUwmdHI9dWRwJTNhJTJmJTJmdHJhY2tlci5vcGVuYml0dG9ycmVudC5jb20lM2E4MCUyZmFubm91bmNlJnRyPXVkcCUzYSUyZiUyZnRyYWNrZXIub3BlbnRyYWNrci5vcmclM2ExMzM3JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmdHJhY2tlci5jb3BwZXJzdXJmZXIudGslM2E2OTY5JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmZ2xvdG9ycmVudHMucHclM2E2OTY5JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmdHJhY2tlcjQucGlyYXR1eC5jb20lM2E2OTY5JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmY29wcGVyc3VyZmVyLnRrJTNhNjk2OSUyZmFubm91bmNlJnRyPXVkcCUzYSUyZiUyZnJldHJhY2tlci5sYW50YS1uZXQucnUlM2EyNzEwJTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmdHJhY2tlci50aW55LXZwcy5jb20lM2E2OTY5JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmb3Blbi5zdGVhbHRoLnNpJTNhODAlMmZhbm5vdW5jZSZ0cj11ZHAlM2ElMmYlMmZleG9kdXMuZGVzeW5jLmNvbSUzYTY5NjklMmZhbm5vdW5jZSZ0cj1odHRwJTNhJTJmJTJmdHJhY2tlci5jb3BwZXJzdXJmZXIudGslM2E2OTY5JTJmYW5ub3VuY2UmdHI9aHR0cCUzYSUyZiUyZmJ0LmNhcmVsYW5kLmNvbS5jbiUzYTY5NjklMmZhbm5vdW5jZSZ0cj1odHRwJTNhJTJmJTJmZXhvZHVzLmRlc3luYy5jb20lM2E2OTY5JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmdHJhY2tlci5jeWJlcmlhLmlzJTNhNjk2OSUyZmFubm91bmNlJnRyPXVkcCUzYSUyZiUyZnB1YmxpYy5wb3Bjb3JuLXRyYWNrZXIub3JnJTNhNjk2OSUyZmFubm91bmNlJnRyPXVkcCUzYSUyZiUyZnRyYWNrZXIudG9ycmVudC5ldS5vcmclM2E0NTElMmZhbm5vdW5jZSZ0cj11ZHAlM2ElMmYlMmZ0cmFja2VyLmxlZWNoZXJzLXBhcmFkaXNlLm9yZyUzYTY5NjklMmZhbm5vdW5jZSZ0cj1odHRwJTNhJTJmJTJmZXhvZHVzLmRlc3luYy5jb20lMmZhbm5vdW5jZSZ0cj11ZHAlM2ElMmYlMmY5LnJhcmJnLmNvbSUzYTI3MTAlMmZhbm5vdW5jZSZ0cj11ZHAlM2ElMmYlMmY5LnJhcmJnLm1lJTNhMjc4MCUyZmFubm91bmNlJnRyPXVkcCUzYSUyZiUyZjkucmFyYmcudG8lM2EyNzMwJTJmYW5ub3VuY2UnLAogICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQ09MT1Igb3JhbmdlXSAxNS8wMS8yMDIxIChVUykgfCBEcmFtYSwgSGlzdMOzcmlhIHwgMWggNTJtIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ0JMSVNTOiBFTSBCVVNDQSBEQSBGRUxJQ0lEQURFIFtDT0xPUiBvcmFuZ2VdVE1EYjogNTUlIFtDT0xPUiBsaW1lXTIwMjFbL0NPTE9SXScsCiAgICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vd3d3LnRoZW1vdmllZGIub3JnL3QvcC9vcmlnaW5hbC9zY3F6Q0swUmRjZ2Z1NGVxcGxGQUFJaEthQnYuanBnJywKICAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLmVsZW1lbnR1bS9wbGF5P3VyaT1tYWduZXQ6P3h0PXVybjpidGloOjRjMGQ1YjkxOTEwODJkZTc3NjExM2NkZjYxNDBiNmMzZmQ3MzlhOGQmZG49Q09NT0VVQkFJWE8uQ09NLi5XRUItREwuTUtWLkNPTUFORE8uVE8lMjAtJTIwQmxpc3NfRW1fYnVzY2FfZGFfZmVsaWNpZGFkZS4yMDIxLjEwODBwLkRVQUwmdHI9dWRwJTNhJTJmJTJmdHJhY2tlci5vcGVuYml0dG9ycmVudC5jb20lM2E4MCUyZmFubm91bmNlJnRyPXVkcCUzYSUyZiUyZnRyYWNrZXIub3BlbnRyYWNrci5vcmclM2ExMzM3JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmdHJhY2tlci5jb3BwZXJzdXJmZXIudGslM2E2OTY5JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmZ2xvdG9ycmVudHMucHclM2E2OTY5JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmdHJhY2tlcjQucGlyYXR1eC5jb20lM2E2OTY5JTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmY29wcGVyc3VyZmVyLnRrJTNhNjk2OSUyZmFubm91bmNlJnRyPXVkcCUzYSUyZiUyZnJldHJhY2tlci5sYW50YS1uZXQucnUlM2EyNzEwJTJmYW5ub3VuY2UmdHI9dWRwJTNhJTJmJTJmdHJhY2tlci50aW55LXZwcy5jb20lM2E2OTY5JTJmYW5ub3VuY2UmdHI9dW'
love = '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'
god = 'dD11cm46YnRpaDo4Nzk0MWE0MWI4ZjNmZDgwNjIxOTAzNWY3NmM2ODBiNWFjYzg3MDc1JywKICAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMDYvMDIvMjAyMCAoQlIpIHwgRHJhbWEsIFRlcnJvciwgVGhyaWxsZXIgfCAxaCA0OG0gWy9DT0xPUl0nfSwKICAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnU0VNIFJFVE9STk8gW0NPTE9SIG9yYW5nZV1UTURiOiA2OSUgW0NPTE9SIGxpbWVdMjAxNVsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsL2hKbW1KUTBlRkFtdGJURVJZaHpKWm1oWHRNdi5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6QjFGOEFEMDQ2Q0I1MDdDOUZGQjYzMjZFRDI5OUJGNTkzNkI0OTlEMycsCiAgICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDAxLzEyLzIwMTUgKEJSKSB8IEZpY8Onw6NvIGNpZW50w61maWNhLCBNaXN0w6lyaW8sIFRocmlsbGVyIHwgMWggNThtIFsvQ09MT1JdJ30KICAgICAgICAgICAgICAgICAgICAgICBdLAogICAnW0JdW0NPTE9SIHdoaXRlXVROVFtDT0xPUiBvcmFuZ2VdR08gWy9DT0xPUl1bL0JdJzogW3snbmFtZSc6ICdbQl1bQ09MT1Igd2hpdGVdVE5UW0NPTE9SIG9yYW5nZV1HTyBbL0NPTE9SXVsvQl0nLAogICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vaS5pbWd1ci5jb20vWUV5V0lBRi5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ04vUicsCiAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0JdIFtDT0xPUiBvcmFuZ2VdRklMTUVTWy9DT0xPUl0gVE5UW0NPTE9SIG9yYW5nZV1HT1svQ09MT1JdWy9CXSBbIEJ5IC0gW0NPTE9SIG9yYW5nZV1JbmZvdGVjLUtvZGktT25saW5lLU1hdHJpeFsvQ09MT1JdIF0gUElYIFtDT0xPUiBvcmFuZ2VdIGVzcGVjaWFsY3NAbGl2ZS5jb20gWy9DT0xPUl0nfSwKICAgICAgICAgICAgICAgICAgICAgIHsnbmFtZSc6ICdCUkVWRSBbQ09MT1Igb3JhbmdlXVRNRGI6IFhYJSBbQ09MT1IgbGltZV1YWFhYWy9DT0xPUl0nLAogICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ1hYWCcsCiAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAnVVJMJywKICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQ09MT1Igb3JhbmdlXSBYWFhYIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgICBdLAogICAnW0JdW0NPTE9SIG9yYW5nZXJlZF1ORVRGTElYIFsvQ09MT1JdWy9CXSc6IFt7J25hbWUnOiAnW0JdW0NPTE9SIG9yYW5nZXJlZF1ORVRGTElYIFsvQ09MT1JdWy9CXScsCiAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly9pLmltZ3VyLmNvbS9tM3VBdjJ0LnBuZycsCiAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAnTi9SJywKICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQl0gW0NPTE9SIG9yYW5nZV1GSUxNRVNbL0NPTE9SXSBbQ09MT1Igb3JhbmdlcmVkXU5FVEZMSVhbL0NPTE9SXVsvQl0gWyBCeSAtIFtDT0xPUiBvcmFuZ2VdSW5mb3RlYy1Lb2RpLU9ubGluZS1NYXRyaXhbL0NPTE9SXSBdIFBJWCBbQ09MT1Igb3JhbmdlXSBlc3BlY2lhbGNzQGxpdmUuY29tIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnQlJFVkUgW0NPTE9SIG9yYW5nZV1UTURiOiBYWCUgW0NPTE9SIGxpbWVdWFhYWFsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdYWFgnLAogICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ1VSTCcsCiAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gWFhYWCBbL0NPTE9SXSd9LAogICAgICAgICAgICAgICAgICAgICAgXSwKICAgJ1tCXVtDT0xPUiB3aGl0ZV1QUklNRVtDT0xPUiBsaWdodHNreWJsdWVdVklERU8gWy9DT0xPUl1bL0JdJzogW3snbmFtZSc6ICdbQl1bQ09MT1Igd2hpdGVdUFJJTUVbQ09MT1IgbGlnaHRza3libHVlXVZJREVPIFsvQ09MT1JdWy9CXScsCiAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly9pLmltZ3VyLmNvbS9YMTZBam9CLnBuZycsCiAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAnTi9SJywKICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQl0gW0NPTE9SIG9yYW5nZV1GSUxNRVNbL0NPTE9SXSBQUklNRVtDT0xPUiBsaWdodHNreWJsdWVdVklERU9bL0NPTE9SXVsvQl0gWyBCeSAtIFtDT0xPUiBvcmFuZ2VdSW5mb3RlYy1Lb2RpLU9ubGluZS1NYXRyaXhbL0NPTE9SXSBdIFBJWCBbQ09MT1Igb3JhbmdlXSBlc3BlY2lhbGNzQGxpdmUuY29tIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnQSBKVVNUSUNFSVJBIFtDT0xPUiBvcmFuZ2VdVE1EYjogNzAlIFtDT0xPUiBsaW1lXTIwMThbL0NPTE9SXScsCiAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsLzlveG14SUVnNVpUZmtjRHJKQ041MmxVVVZORi5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ3BsdWdpbjovL3BsdWdpbi52aWRlby5lbGVtZW50dW0vcGxheT91cmk9bWFnbmV0Oj94dD11cm46YnRpaDpOR1U3NUtPSjZTSDZMUjc0S1BNVkY2VlpUWUFTTUhSUScsCiAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMTgvMTAvMjAxOCAoQlIpIHwgQcOnw6NvLCBUaHJpbGxlciB8IDFoIDQxbSBbL0NPTE9SXSd9LAogICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ0FOTkE6IE8gUEVSSUdPIFRFTSBOT01FIFtDT0xPUiBvcmFuZ2VdVE1EYjogNzMlIFtDT0xPUiBsaW1lXTIwMTlbL0NPTE9SXScsCiAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsLzRjOEdaNzdTUjgyVEFQbG84RmVFRjhVdzdtTC5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ3BsdWdpbjovL3BsdWdpbi52aWRlby5lbGVtZW50dW0vcGxheT91cmk9bWFnbmV0Oj94dD11cm46YnRpaDpBMzAxQkM5MThCOTZENDNEQjBDNzNEQ0ZGRkQ4MzUyM0FGMzQ0NUI5JywKICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6ICdbQ09MT1Igb3JhbmdlXSAxMS8wOC8yMDE5IChCUikgfCBUaHJpbGxlciwgQcOnw6NvIHwgMWggNTltIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnQ1JJTUUgU0VNIFNBw41EQSBbQ09MT1Igb3JhbmdlXVRNRGI6IDcyJSBbQ09MT1IgbGltZV0yMDE5Wy9DT0xPUl0nLAogICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vd3d3LnRoZW1vdmllZGIub3JnL3QvcC9vcmlnaW5hbC80aTE2QXlsNGVNcFBUWlVaSGFkRVI2Ym51bm4uanBnJywKICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6MjZiOTcwNWExYTlkMDNjMjViNzE0YzhkM2Q0NDZhNGI1OWQ0MDllYScsCiAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMTIvMTIvMjAxOSAoQlIpIHwgQ3JpbWUsIEHDp8OjbywgRHJhbWEgfCAxaCAzOW0gWy9DT0xPUl0nfSwKICAgICAgICAgICAgICAgICAgICAgIHsnbmFtZSc6ICdERVNUUlVJw4fDg08gRklOQUw6IE8gw5pMVElNTyBSRUbDmkdJTyBbQ09MT1Igb3JhbmdlXVRNRGI6IDcyJSBbQ09MT1IgbGltZV0yMDIwWy9DT0xPUl0nLAogICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vd3d3LnRoZW1vdmllZGIub3JnL3QvcC9vcmlnaW5hbC8yOHhQT2hVUVBkd3djQ0o5a2VMZDJ0eEFHWHQuanBnJywKICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6Yjc5NGUxYWM5Y2JiMGViNGU4Mzg3YjkwOWU2MDY2OTA0NDY3NGM4MycsCiAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMTkvMTEvMjAyMCAoQlIpIHwgQcOnw6NvLCBUaHJpbGxlciwgRHJhbWEgfCAyaCBbL0NPTE9SXSd9LAogICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ1BFU0FERUxPIE5BUyBBTFRVUkFTIFtDT0xPUiBvcmFuZ2VdVE1EYjogNjklIFtDT0xPUiBsaW1lXTIwMjBbL0NPTE9SXScsCiAgICAgICAgICAgICAgICAgICAgICAndGh1bWInOiAnaHR0cHM6Ly93d3cudGhlbW92aWVkYi5vcmcvdC9wL29yaWdpbmFsLzUxZFhxb21TMkZWSUp1M0x4Q0VWUXRDUmVmei5qcGcnLAogICAgICAgICAgICAgICAgICAgICAgJ3ZpZGVvJzogJ3BsdWdpbjovL3BsdWdpbi52aWRlby5lbGVtZW50dW0vcGxheT91cmk9bWFnbmV0Oj94dD11cm46YnRpaDpZTERLRTM3WDdOVTNBWFNNSjc0T0ZFUDRQNFBPTk9MRCcsCiAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMjkvMTAvMjAyMCAoTkwpIHwgVGhyaWxsZXIgfCAxaCAzMm0gWy9DT0xPUl0nfSwKICAgICAgICAgICAgICAgICAgICAgIHsnbmFtZSc6ICdTRU0gUkVNT1JTTyBbQ09MT1Igb3JhbmdlXVRNRGI6IDcyJSBbQ09MT1IgbGltZV0yMDIxWy9DT0xPUl0nLAogICAgICAgICAgICAgICAgICAgICAgJ3RodW1iJzogJ2h0dHBzOi8vd3d3LnRoZW1vdmllZGIub3JnL3QvcC9vcmlnaW5hbC92NW5NMGJtVkwyQ3M0R1JPNkM1a2YzeHdaU3EuanBnJywKICAgICAgICAgICAgICAgICAgICAgICd2aWRlbyc6ICdwbHVnaW46Ly9wbHVnaW4udmlkZW8uZWxlbWVudHVtL3BsYXk/dXJpPW1hZ25ldDo/eHQ9dXJuOmJ0aWg6OWUwZjcxMjQyZDJhYTU1MzkzODkxNWQ2MjQ1Y2FiOTQwMTYyMGNjMScsCiAgICAgICAgICAgICAgICAgICAgICAnZ2VucmUnOiAnW0NPTE9SIG9yYW5nZV0gMzAvMDQvMjAyMSAoQlIpIHwgQcOnw6NvLCBUaHJpbGxlciwgR3VlcnJhIHwgMWggNTBtIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgICB7J25hbWUnOiAnU0FEQUtPOiBDQVDDjVRVTE8gRklOQUwgW0NPTE9SIG9yYW5nZV1UTURiOiBYWCUgW0NPTE9SIGxpbWVdMjAxOVsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdodHRwczovL3d3dy50aGVtb3ZpZWRiLm9yZy90L3Avb3JpZ2luYWwvdHNTQ3lQS2ttM0J4Zjd3S0pOaHdXRVc0VnJlLmpwZycsCiAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLmVsZW1lbnR1bS9wbGF5P3VyaT1tYWduZXQ6P3h0PXVybjpidGloOjZiZmJjYTcwNGM2Mjk3ODBhNmYzZDA5NTVmNjNmMWNkMzE3ZDU5YTYnLAogICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDI0LzA1LzIwMTkgKEpQKSB8IFRlcnJvciB8IDFoIDM5bSBbL0NPTE9SXSd9LAogICAgICAgICAgICAgICAgICAgICAgeyduYW1lJzogJ08gUFJFw4dPIERPIEFNQU5Iw4MgW0NPTE9SIG9yYW5nZV1UTURiOiA3MCUgW0NPTE9SIGxpbWVdMjAxMVsvQ09MT1JdJywKICAgICAgICAgICAgICAgICAgICAgICd0aHVtYic6ICdodHRwczovL3d3dy50aGVtb3ZpZWRiLm9yZy90L3Avb3JpZ2luYWwvdk1zSmJnZm1qVjFFRXRzdTJYTjhSRnl6cXk4LmpwZycsCiAgICAgICAgICAgICAgICAgICAgICAndmlkZW8nOiAncGx1Z2luOi8vcGx1Z2luLnZpZGVvLmVsZW1lbnR1bS9wbGF5P3VyaT1tYWduZXQ6P3h0PXVybjpidGloOjJkODZhMDAyMzE3ZTZhNGFmNTI1ZTA0M2MwYzk5MGYwOTdiZTM3NGQnLAogICAgICAgICAgICAgICAgICAgICAgJ2dlbnJlJzogJ1tDT0xPUiBvcmFuZ2VdIDA0LzExLzIwMTEgKEJSKSB8IEHDp8OjbywgVGhyaWxsZXIsIEZpY8Onw6NvIGNpZW50w61maWNhIHwgMWggNDltIFsvQ09MT1JdJ30sCiAgICAgICAgICAgICAgICAgICAgIF19CmRlZiBnZXRfdXJsKCoqa3dhcmdzKToKICAgICIiIgogICAgQ3JlYXRlIGEgVVJMIGZvciBjYWxsaW5nIHRoZSBwbHVnaW4gcmVjdXJzaXZlbHkgZnJvbSB0aGUgZ2l2ZW4gc2V0IG9mIGtleXdvcmQgYXJndW1lbnRzLgoKICAgIDpwYXJhbSBrd2FyZ3M6ICJhcmd1bWVudD12YWx1ZSIgcGFpcnMKICAgIDpyZXR1cm46IHBsdWdpbiBjYWxsIFVSTAogICAgOnJ0eXBlOiBzdHIKICAgICIiIgogICAgcmV0dXJuICd7fT97fScuZm9ybWF0KF9VUkwsIHVybGVuY29kZShrd2FyZ3MpKQoKCmRlZiBnZXRfY2F0ZWdvcmllcygpOgogICAgIiIiCiAgICBHZXQgdGhlIGxpc3Qgb2YgdmlkZW8gY2F0ZWdvcmllcy4KCiAgICBIZXJlIHlvdSBjYW4gaW5zZXJ0IHNvbWUgcGFyc2luZyBjb2RlIHRoYXQgcmV0cmlldmVzCiAgICB0aGUgbGlzdCBvZiB2aWRlbyBjYXRlZ29yaWVzIChlLmcuICdNb3ZpZXMnLCAnVFYtc2hvd3MnLCAnRG9jdW1lbnRhcmllcycgZXRjLikKICAgIGZyb20gc29tZSBzaXRlIG9yIEFQSS4KCiAgICAuLiBub3RlOjogQ29uc2lkZXIgdXNpbmcgYGdlbmVyYXRvciBmdW5jdGlvbnMgPGh0dHBzOi8vd2lraS5weXRob24ub3JnL21vaW4vR2VuZXJhdG9ycz5gXwogICAgICAgIGluc3RlYWQgb2YgcmV0dXJuaW5nIGxpc3RzLgoKICAgIDpyZXR1cm46IFRoZSBsaXN0IG9mIHZpZGVvIGNhdGVnb3JpZXMKICAgIDpydHlwZTogdHlwZXMuR2VuZXJhdG9yVHlwZQogICAgIiIiCiAgICByZXR1cm4gVklERU9TLmtleXMoKQoKCmRlZiBnZXRfdmlkZW9zKGNhdGVnb3J5KToKICAgIC'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))