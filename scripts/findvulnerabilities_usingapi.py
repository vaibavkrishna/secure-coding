import requests
import time

def query_nvd(library_name):
    url = f'https://services.nvd.nist.gov/rest/json/cves/1.0?keyword={library_name}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        nvd_data = response.json()
        
        for entry in nvd_data['result']['CVE_Items']:
            print(f"Vulnerability found for {library_name}: {entry['cve']['description']['description_data'][0]['value']}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from NVD: {e}")

libraries = [
    'proxy.h', 'httpd.h', 'ctype.h', 'httpd_ext.h', 'search.h', 'netdb.h', 'errno.h', 'stdio.h',
    'netinet/in.h', 'unistd.h', 'arpa/inet.h', 'www_links.h', 'string.h', 'www.h', 'pthread.h',
    'sys/types.h', 'sys/time.h', 'stdarg.h', 'strings.h', 'proxy_ext.h', 'www_ext.h', 'sys/socket.h',
    'stdlib.h', 'ghostd.h', 'time.h', 'lowlevel.h', 'fcntl.h', 'signal.h', 'http.h', 'daemon.h',
    'elf_ext.h', 'shbuf.h', 'ctype.h', 'stdarg.h', 'elf.h', 'crypt.h', 'time.h', 'string.h', 'fcntl.h',
    'stdio.h', 'asm.h', 'stdlib.h', 'sys/stat.h', 'postprocs.h', 'io.h', 'gizmo.h', 'sys/types.h',
    'gizmos.h', 'unistd.h', 'preprocs.h', 'misc.h', 'shells.h', 'x86.h', 'gfx.h',
    'linux/signal.h', 'linux/slab.h', 'linux/init.h', 'linux/file.h', 'linux/string.h', 'linux/fcntl.h',
    'linux/ptrace.h', 'linux/stat.h', 'linux/module.h', 'linux/errno.h', 'asm/uaccess.h', 'asm/system.h',
    'linux/personality.h', 'linux/kernel.h', 'linux/a.out.h', 'asm/cacheflush.h', 'linux/time.h',
    'linux/fs.h', 'linux/mman.h', 'linux/user.h', 'linux/mm.h', 'linux/binfmts.h',
    'ntddk.h',
    'sys/stat.h', 'utilities.h', 'sys/types.h', 'consts.h', 'process.h', 'errno.h', 'hex_ext.h', 'gfx.h',
    'io_ext.h', 'ctype.h', 'process_ext.h', 'unistd.h', 'string.h', 'sys/wait.h', 'hexdump.h', 'stdarg.h',
    'opts.h', 'sinister.h', 'procfs.h', 'stdlib.h', 'opts_ext.h', 'signal.h', 'io.h', 'stdio.h', 'linux/user.h',
    'sys/ptrace.h'
]

for library in libraries:
    print(library)
    query_nvd(library)
    time.sleep(1)  # Introduce a 1-second gap between requests
    print("-"*64, '\n'*2)
