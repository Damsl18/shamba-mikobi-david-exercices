**QUESTION 1: Navigation et structure Linux**
**Commandes utilisées**:
1. **touch**: permet de créer un fichier
2. **mkdir**: permet de créer un dossier
3. **cd** : permet de se déplacer dans les différents dossiers
4. **tree**: permet de voir l'arborescence du dossier courant
5. **tree projet_linux**: permet de voir l'arborescence du dossier projet_linux
6. **tree projet_linux >> terminal.md**: permet de voir l'arborescence d'un dossier spécifique et de le copié dans le fichier terminal.md
7. **vim**: permet d'ouvrir un éditeur de texte

**RESULTAT DE LA QUESTION 1:**
projet-linux
├── logs
│   ├── fichier1.txt
│   ├── fichier2.txt
│   └── fichier3.txt
├── sauvegardes
├── scripts
│   ├── script1.sh
│   └── script2.sh
└── utilisateurs

5 directories, 5 files

**QUESTION 2: Gestion de permissions**

total 0
-rwxr-x--- 1 dams dams 0 24 mars  18:24 deploy.sh
1. **-**: Montre le type de fichier(Dossier, fichier, etc..), dans notre cas, le type est **fichier**
2. **rwx**: Montre les permissions du propriétaire (user)
3. **r-x**: MOntre les permissions du groupe, **r** pour la lecture, **-** qui signifie qu'il n'a aucune permission d'écriture et **x** pour l'éxécution
4. **- - -**: Montre la permission des autres utilisateurs, dans notre cas, les autres utilisateurs n'ont aucune permission.

**Legende**:
**r**: read, lecture
**w**: write, écriture
**x**: execute, execution

**QUESTION 3: Recherche avancée**
Commandes utilisées:
1. **ls * .log**: **ls** pour permettre de lister * pour afficher tout, et **.log** le critère d'affichage, en gros, **affiche tout les fichiers se terminant avec .log**
2. **find [chemin] -type f -size +5M**: on utilise la commande find pour permettre de trouver le fichier, dans un dossier spécifique, et ce fichier est de type **f** donc un file et sa taille (**-size**) doit être supérieur à 5M (**+5M**)
3. **find [chemin] -type f -mtime 2**: find pour permettre de trouver le fichierdans un dossier spécifique et ce fichier est de type f pour file (fichier normal) et l'argument  **-mtime** va permettre de donner le temps (en joursde 24h).
4. rm * .tmp: **rm** pour supprimer et * pour tout les éléments finissant avec **.tmp**

**QUESTION 4: Analyse de contenu**
1. Pour afficher les 5 premières lignes, j'ai utilisé la commande **head -5 log.txt**
2. pour afficher les 5 denrières lignes, j'ai utilisé la commande **tail -5 log.txt**
3. pour compter le nombre total de lignes, **wc -l log.txt** 
**resultat**: 50 log.txt
4. pour rechercher toutes les lignes contenant le mot ERROR, **grep  "ERROR" log.txt**
**resultat:** 
2026-03-25 09:20:12 vpn-gateway ERROR Failed authentication attempt for user alice from 198.51.100.42
2026-03-25 09:20:28 app-web03 ERROR Database timeout while processing transaction 9821
2026-03-25 09:20:55 server02 ERROR Disk write failure on /dev/sdb3
2026-03-25 09:21:28 switch-core01 ERROR VLAN mismatch detected on trunk port 5
2026-03-25 09:21:49 endpoint-desktop09 ERROR Application crash: outlook.exe terminated unexpectedly
2026-03-25 09:22:22 firewall01 ERROR SSL inspection failed for host example.com
2026-03-25 09:22:42 app-web03 ERROR Failed to fetch API response from internal service
2026-03-25 09:23:15 app-db01 ERROR Query failed on reporting database: timeout
2026-03-25 09:23:42 endpoint-laptop18 ERROR Unauthorized file deletion attempt: C:\Windows\System32\drivers
2026-03-25 09:24:15 ids01 ERROR Threat engine failed to update signatures
2026-03-25 09:25:08 firewall01 ERROR VPN decryption failed for client remote01

5. pour compter combien de fois le mot "SERVER" apparaît, **grep "server" log.txt | wc -l**

**QUESTION 5: Redirection et pipes**
1. Lister tout les fichiers du repertoire courant et rediriger la sortie vers fichiers.txt
i
commande: **ls > fichiers.txt**
2. Ajouter la date dans le même fichier
commande: **date >> fichiers.txt**
3. afficher les lignes contenant .sh
commande: **grep ".sh" fichiers.txt**
4. Compter combien de fichiers .txt existent dans un dossier
commande: **ls * .txt [nom du dossier ou chemmin du dossier ] | wc -l**

**>** : récupère la sortie d'une commande et l'écrit dans un fichier souhaîtée en écrasant tout ce qu'il y avait avant dans le fameu fichier
**>>** :  fait la même chose que **>** mais lui, ajoute des lignes au lieu d'écraser

**QUESTION 6: Processus Linux**
1. Afficher le processus en cours
commande: **ps aux**
Sortie:

USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.2  25020 15456 ?        Ss   11:38   0:01 /sbin/init splash
root           2  0.0  0.0      0     0 ?        S    11:38   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        S    11:38   0:00 [pool_workqueue_release]
root           4  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-rcu_gp]
root           5  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-sync_wq]
root           6  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-kvfree_rcu_reclaim]
root           7  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-slub_flushwq]
root           8  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-netns]
root          10  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/0:0H-events_highpri]
root          12  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/u16:0-ipv6_addrconf]
root          13  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-mm_percpu_wq]
root          14  0.0  0.0      0     0 ?        S    11:38   0:00 [ksoftirqd/0]
root          15  0.0  0.0      0     0 ?        I    11:38   0:00 [rcu_preempt]
root          16  0.0  0.0      0     0 ?        S    11:38   0:00 [rcu_exp_par_gp_kthread_worker/0]
root          17  0.0  0.0      0     0 ?        S    11:38   0:00 [rcu_exp_gp_kthread_worker]
root          18  0.0  0.0      0     0 ?        S    11:38   0:00 [migration/0]
root          19  0.0  0.0      0     0 ?        S    11:38   0:00 [idle_inject/0]
root          20  0.0  0.0      0     0 ?        S    11:38   0:00 [cpuhp/0]
root          21  0.0  0.0      0     0 ?        S    11:38   0:00 [cpuhp/1]
root          22  0.0  0.0      0     0 ?        S    11:38   0:00 [idle_inject/1]
root          23  0.0  0.0      0     0 ?        S    11:38   0:00 [migration/1]
root          24  0.0  0.0      0     0 ?        S    11:38   0:00 [ksoftirqd/1]
root          26  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/1:0H-events_highpri]
root          27  0.0  0.0      0     0 ?        S    11:38   0:00 [cpuhp/2]
root          28  0.0  0.0      0     0 ?        S    11:38   0:00 [idle_inject/2]
root          29  0.0  0.0      0     0 ?        S    11:38   0:00 [migration/2]
root          30  0.0  0.0      0     0 ?        S    11:38   0:00 [ksoftirqd/2]
root          33  0.0  0.0      0     0 ?        S    11:38   0:00 [cpuhp/3]
root          34  0.0  0.0      0     0 ?        S    11:38   0:00 [idle_inject/3]
root          35  0.0  0.0      0     0 ?        S    11:38   0:00 [migration/3]
root          36  0.0  0.0      0     0 ?        S    11:38   0:00 [ksoftirqd/3]
root          38  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/3:0H-events_highpri]
root          39  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/u17:0-events_unbound]
root          40  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/u18:0-events_unbound]
root          41  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/u19:0-events_unbound]
root          42  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/u20:0-events_unbound]
root          44  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/u20:1-events_unbound]
root          46  0.0  0.0      0     0 ?        S    11:38   0:00 [kdevtmpfs]
root          47  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-inet_frag_wq]
root          48  0.0  0.0      0     0 ?        I    11:38   0:00 [rcu_tasks_kthread]
root          49  0.0  0.0      0     0 ?        I    11:38   0:00 [rcu_tasks_rude_kthread]
root          50  0.0  0.0      0     0 ?        I    11:38   0:00 [rcu_tasks_trace_kthread]
root          51  0.0  0.0      0     0 ?        S    11:38   0:00 [kauditd]
root          52  0.0  0.0      0     0 ?        S    11:38   0:00 [khungtaskd]
root          53  0.0  0.0      0     0 ?        S    11:38   0:00 [oom_reaper]
root          55  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-writeback]
root          57  0.0  0.0      0     0 ?        S    11:38   0:00 [kcompactd0]
root          58  0.0  0.0      0     0 ?        SN   11:38   0:00 [ksmd]
root          59  0.0  0.0      0     0 ?        SN   11:38   0:00 [khugepaged]
root          60  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-kblockd]
root          61  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-blkcg_punt_bio]
root          62  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-kintegrityd]
root          63  0.0  0.0      0     0 ?        S    11:38   0:00 [irq/9-acpi]
root          65  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-tpm_dev_wq]
root          66  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-edac-poller]
root          67  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-devfreq_wq]
root          68  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/1:1-events]
root          69  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/0:1H-kblockd]
root          70  0.0  0.0      0     0 ?        S    11:38   0:00 [kswapd0]
root          77  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-kthrotld]
root          79  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-acpi_thermal_pm]
root          80  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/3:1-events]
root          81  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-mld]
root          82  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/3:2-cgroup_destroy]
root          83  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-ipv6_addrconf]
root          84  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/3:1H-kblockd]
root          86  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/u16:1-ipv6_addrconf]
root          90  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-kstrp]
root          96  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/u21:0]
root          97  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/u22:0]
root          98  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/u23:0]
root          99  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/u24:0-ttm]
root         100  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/u25:0-ttm]
root         104  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/u18:1-events_unbound]
root         168  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/u19:1-flush-8:0]
root         172  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/2:1H-kblockd]
root         230  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/1:1H-kblockd]
root         246  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-ata_sff]
root         249  0.0  0.0      0     0 ?        S    11:38   0:00 [scsi_eh_0]
root         250  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-scsi_tmf_0]
root         251  0.0  0.0      0     0 ?        S    11:38   0:00 [scsi_eh_1]
root         252  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-scsi_tmf_1]
root         257  0.0  0.0      0     0 ?        S    11:38   0:00 [scsi_eh_2]
root         258  0.0  0.0      0     0 ?        I<   11:38   0:00 [kworker/R-scsi_tmf_2]
root         260  0.0  0.0      0     0 ?        I    11:38   0:00 [kworker/u20:3-events_unbound]
root         268  0.0  0.0      0     0 ?        S    11:39   0:00 [irq/18-vmwgfx]
root         269  0.0  0.0      0     0 ?        I<   11:39   0:00 [kworker/R-ttm]
root         272  0.0  0.0      0     0 ?        I    11:39   0:00 [kworker/0:2-events]
root         323  0.0  0.0      0     0 ?        S    11:39   0:00 [jbd2/sda1-8]
root         324  0.0  0.0      0     0 ?        I<   11:39   0:00 [kworker/R-ext4-rsv-conversion]
root         387  0.0  0.3  51088 18148 ?        Ss   11:39   0:00 /usr/lib/systemd/systemd-journald
root         398  0.0  0.0      0     0 ?        I    11:39   0:00 [kworker/u17:3-events_unbound]
root         424  0.0  0.2  37452 12140 ?        Ss   11:39   0:00 /usr/lib/systemd/systemd-udevd
root         425  0.0  0.0      0     0 ?        S    11:39   0:00 [psimon]
root         542  0.0  0.1   8388  7684 ?        Ss   11:39   0:00 /usr/sbin/haveged --Foreground --verbose=1
root         552  0.0  0.1 309900  7880 ?        Ssl  11:39   0:00 /usr/libexec/accounts-daemon
message+     554  0.0  0.1  11808  8928 ?        Ss   11:39   0:01 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
polkitd      555  0.0  0.1 383936 11384 ?        Ssl  11:39   0:00 /usr/lib/polkit-1/polkitd --no-debug --log-level=notice
root         558  0.0  0.1  18560  9132 ?        Ss   11:39   0:00 /usr/lib/systemd/systemd-logind
root         596  0.0  0.3 337620 19872 ?        Ssl  11:39   0:00 /usr/sbin/NetworkManager --no-daemon
root         634  0.0  0.0      0     0 ?        I<   11:39   0:00 [kworker/R-rpciod]
root         635  0.0  0.0      0     0 ?        I<   11:39   0:00 [kworker/R-xprtiod]
root         639  0.0  0.2 391060 12420 ?        Ssl  11:39   0:00 /usr/sbin/ModemManager
root         640  0.0  0.0   6876  2660 ?        Ss   11:39   0:00 /usr/sbin/cron -f
root         650  0.1  0.0 352936  2600 ?        Sl   11:39   0:01 /usr/bin/VBoxDRMClient
root         652  0.0  0.0 357252  3400 ?        Sl   11:39   0:00 /usr/sbin/VBoxService
root         717  0.0  0.0      0     0 ?        I<   11:39   0:00 [kworker/u24:1]
root         718  0.0  0.0      0     0 ?        I<   11:39   0:00 [kworker/u25:1]
root         720  0.0  0.1 385348 10440 ?        Ssl  11:39   0:00 /usr/sbin/gdm3
systemd+     769  0.0  0.1  16624  7364 ?        Ss   11:39   0:00 /usr/lib/systemd/systemd-oomd
root         779  0.0  0.0      0     0 ?        S    11:39   0:00 [psimon]
root         780  0.0  0.7 441336 42996 ?        Ssl  11:39   0:00 /usr/libexec/fwupd/fwupd
root         794  0.0  0.2 543932 14064 ?        Ssl  11:39   0:00 /usr/libexec/udisks2/udisksd
rtkit        826  0.0  0.0  21492  3148 ?        SNsl 11:39   0:00 /usr/libexec/rtkit-daemon
root         843  0.0  0.1 318856 10452 ?        Ssl  11:39   0:00 /usr/libexec/upowerd
colord       943  0.0  0.2 317964 15800 ?        Ssl  11:39   0:00 /usr/libexec/colord
pcscd       1113  0.0  0.1 552252  7948 ?        Ssl  11:39   0:00 /usr/sbin/pcscd --foreground --auto-exit
root        1183  0.0  0.1 309596  7440 ?        Ssl  11:39   0:00 /usr/libexec/power-profiles-daemon
root        1194  0.0  0.1  17512  6868 ?        Ss   11:39   0:00 /usr/sbin/wpa_supplicant -u -s -O DIR=/run/wpa_supplicant GROUP=netdev
root        1203  0.0  0.0      0     0 ?        I<   11:39   0:00 [kworker/R-cfg80211]
root        1354  0.0  0.0      0     0 ?        I    11:44   0:00 [kworker/2:0-events]
root        1361  0.0  0.1 172772 10020 ?        Sl   11:47   0:00 gdm-session-worker [pam/gdm-password]
dams        1373  0.0  0.2  23904 15036 ?        Ss   11:47   0:00 /usr/lib/systemd/systemd --user
dams        1375  0.0  0.0  22584  3864 ?        S    11:47   0:00 (sd-pam)
dams        1395  0.0  0.1   9796  6768 ?        Ss   11:47   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
dams        1396  0.0  0.2 103284 13356 ?        S< sl 11:47   0:00 /usr/bin/pipewire
dams        1398  0.0  0.1 183388 10400 ?        SLsl 11:47   0:00 /usr/bin/gnome-keyring-daemon --foreground --components=pkcs11,secrets --control-directory=/run/user/1000/keyring
dams        1399  0.0  0.0   7212  3576 ?        Ss   11:47   0:00 /usr/bin/mpris-proxy
dams        1400  0.0  0.3 415576 19412 ?        S < sl 11:47   0:00 /usr/bin/wireplumber
dams        1402  0.0  0.0  84704  5292 ?        Ssl  11:47   0:00 /usr/bin/pipewire -c filter-chain.conf
dams        1404  0.0  0.2 170376 12180 ?        S < sl 11:47   0:00 /usr/bin/pipewire-pulse
dams        1434  0.0  0.1 168580  6528 tty2     Ssl+ 11:47   0:00 /usr/libexec/gdm-wayland-session /usr/bin/gnome-session
dams        1451  0.0  0.1 165164  6144 tty2     Sl+  11:47   0:00 /usr/libexec/gnome-session-init-worker gnome
root        1481  0.0  0.0      0     0 ?        I    11:47   0:00 [kworker/1:0-events]
dams        1483  0.0  0.1  97444  7160 ?        Ssl  11:47   0:00 /usr/libexec/gcr-ssh-agent --base-dir /run/user/1000/gcr
dams        1484  0.0  0.0  87248  5088 ?        Ssl  11:47   0:00 /usr/libexec/gnome-session-ctl --monitor
dams        1485  0.0  0.1  10556  6468 ?        Ss   11:47   0:00 /usr/bin/ssh-agent -D
dams        1500  0.0  0.1 313308  8424 ?        Ssl  11:47   0:00 /usr/libexec/gvfsd
root        1507  0.0  0.0      0     0 ?        I <   11:47   0:00 [kworker/2:0H-kblockd]
dams        1513  0.0  0.1 398584  7716 ?        Sl   11:47   0:00 /usr/libexec/gvfsd-fuse /run/user/1000/gvfs -f
dams        1521  0.0  0.1 673960  9912 ?        Ssl  11:47   0:00 /usr/libexec/gnome-session-service --session=gnome
root        1526  0.0  0.0      0     0 ?        I    11:47   0:00 [kworker/u17:2-events_unbound]
dams        1530 12.2  8.6 5218584 502808 ?      Rsl  11:47   1:29 /usr/bin/gnome-shell
dams        1557  0.0  0.1 381176  7356 ?        Ssl  11:47   0:00 /usr/libexec/at-spi-bus-launcher
dams        1564  0.0  0.0   8212  4656 ?        S    11:47   0:00 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 13 --address=unix:path=/run/user/1000/at-spi/bus
dams        1566  0.0  0.1 168772  7016 ?        Sl   11:47   0:00 /usr/libexec/at-spi2-registryd --use-gnome-session
dams        1572  0.0  0.1 165276  6036 ?        Ssl  11:47   0:00 /usr/libexec/dconf-service
dams        1581  0.0  0.1 309064  6928 ?        Ssl  11:47   0:00 /usr/libexec/xdg-permission-store
dams        1583  0.0  0.4 662804 23392 ?        Sl   11:47   0:00 /usr/libexec/gnome-shell-calendar-server
dams        1601  0.0  1.0 826084 62504 ?        Ssl  11:47   0:00 /usr/libexec/evolution-source-registry
dams        1604  0.0  0.5 2662448 32160 ?       Sl   11:47   0:00 /usr/bin/gjs -m /usr/share/gnome-shell/org.gnome.Shell.Notifications
dams        1609  0.0  0.1 247736  8832 ?        Ssl  11:47   0:00 /usr/libexec/gsd-a11y-settings
dams        1610  0.0  0.1 309920  9012 ?        Sl   11:47   0:00 ibus-daemon --panel disable
dams        1611  0.0  0.1 245696  8624 ?        Ssl  11:47   0:00 /usr/libexec/gsd-color
dams        1614  0.0  0.1 254508 10536 ?        Ssl  11:47   0:00 /usr/libexec/gsd-datetime
dams        1618  0.0  0.1 384228  8992 ?        Ssl  11:47   0:00 /usr/libexec/gsd-housekeeping
dams        1621  0.0  0.1 382500  7844 ?        Ssl  11:47   0:00 /usr/libexec/gsd-keyboard
dams        1622  0.0  0.2 684692 12912 ?        Ssl  11:47   0:00 /usr/libexec/gsd-media-keys
dams        1624  0.0  0.1 461124  9640 ?        Ssl  11:47   0:00 /usr/libexec/gsd-power
dams        1626  0.0  0.2 321092 11680 ?        Ssl  11:47   0:00 /usr/libexec/gsd-print-notifications
dams        1628  0.0  1.4 1058416 85644 ?       Sl   11:47   0:00 /usr/libexec/evolution-data-server/evolution-alarm-notify
dams        1629  0.0  0.1 456324  7744 ?        Ssl  11:47   0:00 /usr/libexec/gsd-rfkill
dams        1640  1.1  1.2 906468 75460 ?        Sl   11:47   0:08 /usr/bin/kdeconnectd
dams        1646  0.0  0.1 169224  7052 ?        Ssl  11:47   0:00 /usr/libexec/gsd-screensaver-proxy
dams        1648  0.0  1.1 609976 67084 ?        Sl   11:47   0:00 /usr/bin/python3 /usr/bin/blueman-applet
dams        1651  0.0  0.2 401372 12308 ?        Ssl  11:47   0:00 /usr/libexec/gsd-sharing
dams        1655  0.0  0.2 395292 14232 ?        Ssl  11:47   0:00 /usr/libexec/gsd-smartcard
dams        1657  0.0  0.1 253932 10036 ?        Ssl  11:47   0:00 /usr/libexec/gsd-sound
dams        1658  0.0  0.1 306276  7300 ?        Sl   11:47   0:00 /usr/libexec/gsd-disk-utility-notify
dams        1662  0.0  0.1 465664  8128 ?        Ssl  11:47   0:00 /usr/libexec/gsd-usb-protection
dams        1665  0.0  2.8 1730256 165896 ?      Sl   11:47   0:00 /usr/bin/xwaylandvideobridge
dams        1709  0.0  0.1 389616 10208 ?        Ssl  11:47   0:00 /usr/libexec/gsd-wwan
dams        1759  0.0  0.1 393956 10524 ?        Sl   11:47   0:00 /usr/libexec/gsd-printer
dams        1804  0.0  0.3 1040624 20572 ?       Ssl  11:47   0:00 /usr/libexec/xdg-desktop-portal
dams        1839  0.0  0.5 2597932 32112 ?       Sl   11:47   0:00 /usr/bin/gjs -m /usr/share/gnome-shell/org.gnome.ScreenSaver
dams        1865  0.0  0.5 883184 33140 ?        SNsl 11:47   0:00 /usr/libexec/localsearch-3
dams        1880  0.0  0.5 463576 30720 ?        Sl   11:47   0:00 /usr/libexec/goa-daemon
dams        1885  0.0  0.1 613760  7404 ?        Ssl  11:47   0:00 /usr/libexec/xdg-document-portal
root        1894  0.0  0.0   2592  1948 ?        Ss   11:47   0:00 fusermount3 -o rw,nosuid,nodev,fsname=portal,auto_unmount,subtype=portal -- /run/user/1000/doc
dams        1898  0.0  0.9 766064 55624 ?        Ssl  11:47   0:00 /usr/libexec/xdg-desktop-portal-gnome
dams        1905  0.0  0.1 387992  9784 ?        Sl   11:47   0:00 /usr/libexec/goa-identity-service
dams        1913  0.0  0.4 894348 26724 ?        Ssl  11:47   0:00 /usr/libexec/evolution-calendar-factory
dams        1927  0.0  0.5 828088 31108 ?        Ssl  11:47   0:00 /usr/libexec/evolution-addressbook-factory
dams        1930  0.0  1.2 228048 74360 ?        S    11:47   0:00 /usr/bin/Xwayland :0 -rootless -noreset -accessx -core -auth /run/user/1000/.mutter-Xwaylandauth.Z6XYM3 -listenfd 4 -listenfd 5 -displayfd 6 -initfd 7 -byteswappedclients
dams        1938  0.0  0.1 391152 11496 ?        Ssl  11:47   0:00 /usr/libexec/gvfs-udisks2-volume-monitor
dams        1950  0.0  0.1 308040  6880 ?        Ssl  11:47   0:00 /usr/libexec/gvfs-goa-volume-monitor
dams        1958  0.0  0.1 309032  7388 ?        Ssl  11:47   0:00 /usr/libexec/gvfs-gphoto2-volume-monitor
dams        1963  0.0  0.1 308064  6928 ?        Ssl  11:47   0:00 /usr/libexec/gvfs-mtp-volume-monitor
dams        1968  0.0  0.1 390120  9112 ?        Ssl  11:47   0:00 /usr/libexec/gvfs-afc-volume-monitor
dams        2049  0.0  2.4 1436320 142060 ?      Sl   11:47   0:00 /usr/libexec/mutter-x11-frames
dams        2050  0.2  0.1 385932 11392 ?        Sl   11:47   0:01 ibus-daemon --panel disable -r --xim
dams        2052  0.0  0.0  16724  1756 ?        S    11:47   0:00 /usr/bin/VBoxClient --clipboard
dams        2053  0.0  0.0 215608  4360 ?        Sl   11:47   0:00 /usr/bin/VBoxClient --clipboard
dams        2060  0.0  0.1 387272  9160 ?        Sl   11:47   0:00 /usr/libexec/gvfsd-recent --spawner :1.16 /org/gtk/gvfs/exec_spaw/0
dams        2063  0.0  0.1 534760  9552 ?        Sl   11:47   0:00 /usr/libexec/gvfsd-trash --spawner :1.16 /org/gtk/gvfs/exec_spaw/1
dams        2103  0.0  0.0  16724  1732 ?        S    11:47   0:00 /usr/bin/VBoxClient --vmsvga-session
dams        2107  0.0  0.0 148828  2332 ?        Sl   11:47   0:00 /usr/bin/VBoxClient --vmsvga-session
dams        2124  0.0  0.1 169404  7480 ?        Sl   11:47   0:00 /usr/libexec/ibus-memconf
dams        2130  0.0  0.2 178700 12776 ?        Sl   11:47   0:00 /usr/libexec/ibus-x11 --kill-daemon
dams        2132  0.0  0.1 308752  7700 ?        Sl   11:47   0:00 /usr/libexec/ibus-portal
dams        2169  0.0  0.3 456664 22892 ?        Ssl  11:47   0:00 /usr/libexec/bluetooth/obexd
dams        2172  0.0  0.1 169532  8104 ?        Sl   11:47   0:00 /usr/libexec/ibus-engine-simple
root        2220  0.0  0.0      0     0 ?        I    11:47   0:00 [kworker/u18:2-events_unbound]
dams        2282  0.0  1.1 2851796 66412 ?       Sl   11:47   0:00 gjs /usr/share/gnome-shell/extensions/ding@rastersoft.com/app/ding.js -E -P /usr/share/gnome-shell/extensions/ding@rastersoft.com/app
dams        2333  0.0  0.5 490196 30644 ?        Ssl  11:47   0:00 /usr/libexec/xdg-desktop-portal-gtk
dams        2344  0.0  0.1 169120  6980 ?        Ssl  11:47   0:00 /usr/libexec/gvfsd-metadata
dams        2446  0.0  0.6 535376 35360 ?        Sl   11:47   0:00 gnome-terminal --wait
dams        2456  0.7  1.1 569336 65480 ?        Ssl  11:47   0:05 /usr/libexec/gnome-terminal-server

2. Pour trouver un processus par son nom
commande: **pgrep [le nom du processus]**

3. La différence entre PID et PPID
**PID** c'est l'id d'un processus en cours tandisque **PPID** c'est l'id du processus parent qui a créé ce processus

4. commande pour arreter un processus correctement: **kill [id du processus ou PID]**
5. pour forcer l'arrêt d'un processus: **kill -9 [id du processus ou PID]**


**QUESTION 7: Gestion disque et espace**
1. Afficher l'espace disque total et disponible
commande: **df -h**
Sortie: 
Sys. de fichiers Taille Utilisé Dispo Uti% Monté sur
udev               2,7G       0  2,7G   0% /dev
tmpfs              569M    1,2M  568M   1% /run
/dev/sda1           47G     18G   27G  40% /
tmpfs              2,8G    4,0K  2,8G   1% /dev/shm
none               1,0M       0  1,0M   0% /run/credentials/systemd-journald.service
tmpfs              2,8G     20K  2,8G   1% /tmp
tmpfs              569M    176K  569M   1% /run/user/1000

2. la taille d'un dossier precis
commande: **du -sh projet-linux**
sortie: 
20K	projet-linux

3. identifier les cinq plus gros repertoires
Dans mon cas, je vais identifier les cinq plus gros dans le dossier courant
commande: **du -h ./ | sort -rh | head -5** 
sortie: 
159M	./
98M	./.cache
79M	./.cache/mozilla/firefox/qiwuny1v.default-esr
79M	./.cache/mozilla/firefox
79M	./.cache/mozilla

**QUESTION 8: Utilisateurs et groupes**
1. Créationd d'un nouvel utilisateur
commande: **sudo useradd julie**
2. création d'un groupe nommé devops
commande: **sudo groupadd devops**
3. ajouter un utilisateur au groupe
commande: **sudo usermod -aG devops julie**
4. verifier les groupes d'un utilisateur
commande: **groups julie**
5. **Elle va permettre de contrôler l'accès à différents fichiers ou informations en incluant des privilèges**

**FIN DE LA PARTIE LINUX ET TERMINAL**
