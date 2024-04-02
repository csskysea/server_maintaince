# Lithium nodes information maintain.

- collect lithium nodes information such as mac address,ram size,type,cpu into one excel file.
- run main.py to parse excel file,then update dhcpd conf,hosts file,and slurm conf.
- restart dhcpd service and slurm daemons to make configuration take effect.


# others you need to know.

to let all lithium use one hosts file and one slurm configuration, you need prepare a directory in
ceph fs and mount it as `/etc/lithium` in lithium rbd image and create symbol links to hosts file and slurm conf.

currently, I placed `lithium conf` in `/home/public`

```bash
lithium_conf/
├── hosts_conf
│   └── hosts
└── slurm_conf
    ├── cgroup
    │   ├── release_cpuset
    │   ├── release_freezer
    │   └── release_memory
    ├── cgroup_allowed_devices_file.conf.example
    ├── cgroup.conf.example
    ├── cgroup.release_common.example
    ├── slurm.conf
    ├── slurm.conf.example
    ├── slurm.conf.org
    └── slurm.epilog.clean
```

in `lithium` node:

```
fstab:
172.16.100.152,172.16.100.153:/home/public/lithium_conf    /etc/lithium_conf    ceph  name=fsmounter,secret=AQBiXrtWt+ZcHxAAh2tA+HQsCOd0liYSeJ8q8A==,_netdev
```

```
symbol links:
lrwxrwxrwx.  1 root   root     24 7月   1 16:42 slurm -> lithium_conf/slurm_conf/
lrwxrwxrwx.  1 root   root     29 7月   1 16:41 hosts -> lithium_conf/hosts_conf/hosts
```


# usage


./main.py [excel file] [shared directory which exists hosts and slurm conf.]
eg. ./main.py rack_map.xlsx /home/public/lithium_conf