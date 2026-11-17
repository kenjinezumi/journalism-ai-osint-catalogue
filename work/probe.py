import json,subprocess,sys
def gh(p):
    r=subprocess.run(['gh','api',p],capture_output=True,text=True)
    if r.returncode!=0: return None
    try: return json.loads(r.stdout)
    except: return None
for r in sys.argv[1:]:
    d=gh(f'repos/{r}')
    if not d or 'full_name' not in d: print(f'{r}: NOT FOUND'); continue
    lic=(d.get('license') or {})
    rel=gh(f'repos/{r}/releases/latest') or {}
    print(f"{r} -> {d['full_name']} | spdx={lic.get('spdx_id')} ({lic.get('name')}) | archived={d.get('archived')} | pushed={d.get('pushed_at','')[:10]} | stars={d.get('stargazers_count')} | rel={rel.get('tag_name')} {str(rel.get('published_at'))[:10]} | fork={d.get('fork')} parent={(d.get('parent') or {}).get('full_name')}")
