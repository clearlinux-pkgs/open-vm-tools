#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : open-vm-tools
Version  : 10.3.5
Release  : 26
URL      : https://github.com/vmware/open-vm-tools/releases/download/stable-10.3.5/open-vm-tools-10.3.5-10430147.tar.gz
Source0  : https://github.com/vmware/open-vm-tools/releases/download/stable-10.3.5/open-vm-tools-10.3.5-10430147.tar.gz
Source1  : open-vm-tools.service
Summary  : Library for unpacking and executing VMware Guest Customization package.
Group    : Development/Tools
License  : BSD-2-Clause CDDL-1.0 GPL-2.0 LGPL-2.1 MIT
Requires: open-vm-tools-autostart = %{version}-%{release}
Requires: open-vm-tools-bin = %{version}-%{release}
Requires: open-vm-tools-config = %{version}-%{release}
Requires: open-vm-tools-data = %{version}-%{release}
Requires: open-vm-tools-lib = %{version}-%{release}
Requires: open-vm-tools-license = %{version}-%{release}
Requires: open-vm-tools-services = %{version}-%{release}
Requires: fuse
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : compat-fuse-soname2-dev
BuildRequires : doxygen
BuildRequires : fuse-dev
BuildRequires : gettext-bin
BuildRequires : glib-dev
BuildRequires : graphviz
BuildRequires : gtk3-dev
BuildRequires : libSM-dev
BuildRequires : libXext-dev
BuildRequires : libmspack-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : openssl-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libtirpc)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xtst)
BuildRequires : procps-ng-dev
BuildRequires : sed
BuildRequires : xmlsec1-dev
Patch1: 0001-Enable-package-to-build.patch
Patch2: 0002-Stateless.patch
Patch3: 0003-Modify-wakeups-to-be-more-power-friendly.patch

%description
This file is no longer distributed with open-vm-tools.
For current project information and release notes, please refer to

%package autostart
Summary: autostart components for the open-vm-tools package.
Group: Default

%description autostart
autostart components for the open-vm-tools package.


%package bin
Summary: bin components for the open-vm-tools package.
Group: Binaries
Requires: open-vm-tools-data = %{version}-%{release}
Requires: open-vm-tools-config = %{version}-%{release}
Requires: open-vm-tools-license = %{version}-%{release}
Requires: open-vm-tools-services = %{version}-%{release}

%description bin
bin components for the open-vm-tools package.


%package config
Summary: config components for the open-vm-tools package.
Group: Default

%description config
config components for the open-vm-tools package.


%package data
Summary: data components for the open-vm-tools package.
Group: Data

%description data
data components for the open-vm-tools package.


%package dev
Summary: dev components for the open-vm-tools package.
Group: Development
Requires: open-vm-tools-lib = %{version}-%{release}
Requires: open-vm-tools-bin = %{version}-%{release}
Requires: open-vm-tools-data = %{version}-%{release}
Provides: open-vm-tools-devel = %{version}-%{release}

%description dev
dev components for the open-vm-tools package.


%package doc
Summary: doc components for the open-vm-tools package.
Group: Documentation

%description doc
doc components for the open-vm-tools package.


%package extras
Summary: extras components for the open-vm-tools package.
Group: Default

%description extras
extras components for the open-vm-tools package.


%package lib
Summary: lib components for the open-vm-tools package.
Group: Libraries
Requires: open-vm-tools-data = %{version}-%{release}
Requires: open-vm-tools-license = %{version}-%{release}

%description lib
lib components for the open-vm-tools package.


%package license
Summary: license components for the open-vm-tools package.
Group: Default

%description license
license components for the open-vm-tools package.


%package services
Summary: services components for the open-vm-tools package.
Group: Systemd services

%description services
services components for the open-vm-tools package.


%prep
%setup -q -n open-vm-tools-10.3.5-10430147
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546268181
%reconfigure --disable-static --without-gtkmm \
--without-dnet \
--without-gtkmm3 \
--without-gtk2 \
--with-gtk3 \
--with-pam-prefix=/usr/share \
--sysconfdir=/usr/share/defaults/open-vm-tools \
--without-xerces \
--disable-vgauth \
--disable-caf \
--disable-glibc-check
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1546268181
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/open-vm-tools
cp COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/COPYING
cp LICENSE %{buildroot}/usr/share/package-licenses/open-vm-tools/LICENSE
cp checkvm/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/checkvm_COPYING
cp guestproxycerttool/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/guestproxycerttool_COPYING
cp hgfsclient/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/hgfsclient_COPYING
cp hgfsmounter/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/hgfsmounter_COPYING
cp lib/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/lib_COPYING
cp libDeployPkg/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/libDeployPkg_COPYING
cp libguestlib/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/libguestlib_COPYING
cp libhgfs/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/libhgfs_COPYING
cp libvmtools/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/libvmtools_COPYING
cp m4/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/m4_COPYING
cp modules/freebsd/vmblock/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/modules_freebsd_vmblock_COPYING
cp modules/freebsd/vmmemctl/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/modules_freebsd_vmmemctl_COPYING
cp modules/solaris/vmblock/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/modules_solaris_vmblock_COPYING
cp modules/solaris/vmhgfs/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/modules_solaris_vmhgfs_COPYING
cp modules/solaris/vmmemctl/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/modules_solaris_vmmemctl_COPYING
cp modules/solaris/vmxnet/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/modules_solaris_vmxnet_COPYING
cp modules/solaris/vmxnet3/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/modules_solaris_vmxnet3_COPYING
cp namespacetool/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/namespacetool_COPYING
cp rpctool/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/rpctool_COPYING
cp scripts/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/scripts_COPYING
cp services/plugins/deployPkg/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_deployPkg_COPYING
cp services/plugins/desktopEvents/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_desktopEvents_COPYING
cp services/plugins/dndcp/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_dndcp_COPYING
cp services/plugins/grabbitmqProxy/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_grabbitmqProxy_COPYING
cp services/plugins/guestInfo/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_guestInfo_COPYING
cp services/plugins/hgfsServer/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_hgfsServer_COPYING
cp services/plugins/powerOps/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_powerOps_COPYING
cp services/plugins/resolutionKMS/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_resolutionKMS_COPYING
cp services/plugins/resolutionSet/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_resolutionSet_COPYING
cp services/plugins/timeSync/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_timeSync_COPYING
cp services/plugins/vix/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_vix_COPYING
cp services/plugins/vmbackup/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_plugins_vmbackup_COPYING
cp services/vmtoolsd/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/services_vmtoolsd_COPYING
cp tests/testDebug/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/tests_testDebug_COPYING
cp tests/testPlugin/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/tests_testPlugin_COPYING
cp tests/testVmblock/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/tests_testVmblock_COPYING
cp tests/vmrpcdbg/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/tests_vmrpcdbg_COPYING
cp toolbox/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/toolbox_COPYING
cp vgauth/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/vgauth_COPYING
cp vmblock-fuse/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/vmblock-fuse_COPYING
cp vmblockmounter/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/vmblockmounter_COPYING
cp vmhgfs-fuse/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/vmhgfs-fuse_COPYING
cp vmware-user-suid-wrapper/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/vmware-user-suid-wrapper_COPYING
cp xferlogs/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/xferlogs_COPYING
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/open-vm-tools.service
## install_append content
rm %{buildroot}/sbin/mount.vmhgfs
mkdir -p %{buildroot}//usr/lib/systemd/system/multi-user.target.wants
ln -s ../open-vm-tools.service  %{buildroot}//usr/lib/systemd/system/multi-user.target.wants
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/open-vm-tools.service

%files bin
%defattr(-,root,root,-)
/usr/bin/mount.vmhgfs
/usr/bin/vmhgfs-fuse
/usr/bin/vmtoolsd
/usr/bin/vmware-checkvm
/usr/bin/vmware-guestproxycerttool
/usr/bin/vmware-hgfsclient
/usr/bin/vmware-namespace-cmd
/usr/bin/vmware-rpctool
/usr/bin/vmware-toolbox-cmd
/usr/bin/vmware-user
/usr/bin/vmware-user-suid-wrapper
/usr/bin/vmware-vmblock-fuse
/usr/bin/vmware-xferlogs

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/99-vmware-scsi-udev.rules

%files data
%defattr(-,root,root,-)
/usr/share/defaults/open-vm-tools/vmware-tools/guestproxy-ssl.conf
/usr/share/defaults/open-vm-tools/vmware-tools/poweroff-vm-default
/usr/share/defaults/open-vm-tools/vmware-tools/poweron-vm-default
/usr/share/defaults/open-vm-tools/vmware-tools/resume-vm-default
/usr/share/defaults/open-vm-tools/vmware-tools/scripts/vmware/network
/usr/share/defaults/open-vm-tools/vmware-tools/statechange.subr
/usr/share/defaults/open-vm-tools/vmware-tools/suspend-vm-default
/usr/share/defaults/open-vm-tools/vmware-tools/vm-support
/usr/share/defaults/open-vm-tools/xdg/autostart/vmware-user.desktop
/usr/share/open-vm-tools/messages/de/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/de/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/ja/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/ja/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/ko/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/ko/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/zh_CN/toolboxcmd.vmsg
/usr/share/pam.d/vmtoolsd

%files dev
%defattr(-,root,root,-)
/usr/include/libDeployPkg/deploypkg.h
/usr/include/libDeployPkg/guestcust-events.h
/usr/include/libDeployPkg/guestrpc.h
/usr/include/libDeployPkg/imgcust-api.h
/usr/include/libDeployPkg/includeCheck.h
/usr/include/libDeployPkg/linuxDeployment.h
/usr/include/libDeployPkg/log.h
/usr/include/libDeployPkg/process.h
/usr/include/libDeployPkg/vm_basic_types.h
/usr/include/vmGuestLib/includeCheck.h
/usr/include/vmGuestLib/vmGuestLib.h
/usr/include/vmGuestLib/vmSessionId.h
/usr/include/vmGuestLib/vm_basic_types.h
/usr/lib64/libDeployPkg.so
/usr/lib64/libguestlib.so
/usr/lib64/libhgfs.so
/usr/lib64/libvmtools.so
/usr/lib64/pkgconfig/libDeployPkg.pc
/usr/lib64/pkgconfig/vmguestlib.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/open\-vm\-tools/*

%files extras
%defattr(-,root,root,-)
/usr/lib64/open-vm-tools/plugins/vmusr/libdesktopEvents.so
/usr/lib64/open-vm-tools/plugins/vmusr/libresolutionSet.so

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/open-vm-tools/plugins/vmusr/libdesktopEvents.so
%exclude /usr/lib64/open-vm-tools/plugins/vmusr/libresolutionSet.so
/usr/lib64/libDeployPkg.so.0
/usr/lib64/libDeployPkg.so.0.0.0
/usr/lib64/libguestlib.so.0
/usr/lib64/libguestlib.so.0.0.0
/usr/lib64/libhgfs.so.0
/usr/lib64/libhgfs.so.0.0.0
/usr/lib64/libvmtools.so.0
/usr/lib64/libvmtools.so.0.0.0
/usr/lib64/open-vm-tools/plugins/common/libhgfsServer.so
/usr/lib64/open-vm-tools/plugins/common/libvix.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libdeployPkgPlugin.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libgrabbitmqProxy.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libguestInfo.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libpowerOps.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libresolutionKMS.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libtimeSync.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libvmbackup.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/open-vm-tools/COPYING
/usr/share/package-licenses/open-vm-tools/LICENSE
/usr/share/package-licenses/open-vm-tools/checkvm_COPYING
/usr/share/package-licenses/open-vm-tools/guestproxycerttool_COPYING
/usr/share/package-licenses/open-vm-tools/hgfsclient_COPYING
/usr/share/package-licenses/open-vm-tools/hgfsmounter_COPYING
/usr/share/package-licenses/open-vm-tools/libDeployPkg_COPYING
/usr/share/package-licenses/open-vm-tools/lib_COPYING
/usr/share/package-licenses/open-vm-tools/libguestlib_COPYING
/usr/share/package-licenses/open-vm-tools/libhgfs_COPYING
/usr/share/package-licenses/open-vm-tools/libvmtools_COPYING
/usr/share/package-licenses/open-vm-tools/m4_COPYING
/usr/share/package-licenses/open-vm-tools/modules_freebsd_vmblock_COPYING
/usr/share/package-licenses/open-vm-tools/modules_freebsd_vmmemctl_COPYING
/usr/share/package-licenses/open-vm-tools/modules_solaris_vmblock_COPYING
/usr/share/package-licenses/open-vm-tools/modules_solaris_vmhgfs_COPYING
/usr/share/package-licenses/open-vm-tools/modules_solaris_vmmemctl_COPYING
/usr/share/package-licenses/open-vm-tools/modules_solaris_vmxnet3_COPYING
/usr/share/package-licenses/open-vm-tools/modules_solaris_vmxnet_COPYING
/usr/share/package-licenses/open-vm-tools/namespacetool_COPYING
/usr/share/package-licenses/open-vm-tools/rpctool_COPYING
/usr/share/package-licenses/open-vm-tools/scripts_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_deployPkg_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_desktopEvents_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_dndcp_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_grabbitmqProxy_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_guestInfo_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_hgfsServer_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_powerOps_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_resolutionKMS_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_resolutionSet_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_timeSync_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_vix_COPYING
/usr/share/package-licenses/open-vm-tools/services_plugins_vmbackup_COPYING
/usr/share/package-licenses/open-vm-tools/services_vmtoolsd_COPYING
/usr/share/package-licenses/open-vm-tools/tests_testDebug_COPYING
/usr/share/package-licenses/open-vm-tools/tests_testPlugin_COPYING
/usr/share/package-licenses/open-vm-tools/tests_testVmblock_COPYING
/usr/share/package-licenses/open-vm-tools/tests_vmrpcdbg_COPYING
/usr/share/package-licenses/open-vm-tools/toolbox_COPYING
/usr/share/package-licenses/open-vm-tools/vgauth_COPYING
/usr/share/package-licenses/open-vm-tools/vmblock-fuse_COPYING
/usr/share/package-licenses/open-vm-tools/vmblockmounter_COPYING
/usr/share/package-licenses/open-vm-tools/vmhgfs-fuse_COPYING
/usr/share/package-licenses/open-vm-tools/vmware-user-suid-wrapper_COPYING
/usr/share/package-licenses/open-vm-tools/xferlogs_COPYING

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/open-vm-tools.service
/usr/lib/systemd/system/open-vm-tools.service
