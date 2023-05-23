###-----------uos手动打包说明

##-------------先找到一个现成已经打好的uos的deb，如test.deb
#用ar命令解压deb包
ar -x test.deb
#会得到三个文件 control.tar.xz data.tar.xz debian-binary
#使用tar -xvf解压缩control.tar.xz文件
#control.tar.xz中包含control md5sums postinst postrm四个文件

##--------------control中包含要制作的安装包的基本信息，需要更新
#md5sums中包含要安装到系统中文件的md5值，好像写不写，或者对不对都无所谓=.=!
#postinst中包含安装的初始化脚本，通常包括在/usr/local/bin下创建可执行程序的软链接、修改可执行程序的权限等
#postrm中包含软件卸载的脚本，通常包括删除文件等
#可根据实际的情况更新编辑相应的文件

#使用tar -Jcf control.tar.xz control md5sums postinst postrm命令重新打包压缩 control.tar.xz文件

##----------------使用tar -xvf解压缩data.tar.xz文件
#data.tar.xz中包含/opt/apps/com.deepin.xxx/目录，此目录下包含 entries/、files/、info两个文件夹和一个文件
#entries中包含5个目录，目前只需要更新applications目录下的.desktop文件即可，其他目录可忽略

#files中包含要安装的程序文件，即build之后需要copy到系统中的文件
#build成功后手动更新相应文件即可
#info文件中写的是此程序的包信息，手动编辑更新即可

#使用tar -Jcf data.tar.xz opt命令重新打包压缩 data.tar.xz文件


##-------------------control.tar.xz和data.tar.xz更新完成后即可重新打包deb文件
#使用ar rcs test.deb debian-binary control.tar.xz data.tar.xz命令即可打包deb文件


