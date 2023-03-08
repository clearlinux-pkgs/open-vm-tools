#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : open-vm-tools
Version  : 12.2.0
Release  : 44
URL      : https://github.com/vmware/open-vm-tools/releases/download/stable-12.2.0/open-vm-tools-12.2.0-21223074.tar.gz
Source0  : https://github.com/vmware/open-vm-tools/releases/download/stable-12.2.0/open-vm-tools-12.2.0-21223074.tar.gz
Source1  : open-vm-tools.service
Source2  : vmware-vmblock-fuse.service
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
Requires: open-vm-tools-setuid = %{version}-%{release}
Requires: fuse
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : compat-fuse-soname2-dev
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : fuse-dev
BuildRequires : gdk-pixbuf-xlib-dev
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
BuildRequires : pkgconfig(gtkmm-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libtirpc)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xtst)
BuildRequires : procps-ng-dev
BuildRequires : protobuf-dev
BuildRequires : sed
BuildRequires : valgrind
BuildRequires : xmlsec1-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
Requires: open-vm-tools-setuid = %{version}-%{release}
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
Requires: open-vm-tools = %{version}-%{release}

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
Requires: /usr/bin/modprobe

%description services
services components for the open-vm-tools package.


%package setuid
Summary: setuid components for the open-vm-tools package.
Group: Default

%description setuid
setuid components for the open-vm-tools package.


%prep
%setup -q -n open-vm-tools-12.2.0-21223074
cd %{_builddir}/open-vm-tools-12.2.0-21223074
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678293240
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%reconfigure --disable-static --without-dnet \
--without-gtk2 \
--with-gtk3 \
--with-pam-prefix=/usr/share \
--sysconfdir=/usr/share/defaults/open-vm-tools \
--without-xerces \
--disable-vgauth \
--disable-caf \
--disable-glibc-check \
--disable-tests \
--without-kernel-modules
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1678293240
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/open-vm-tools
cp %{_builddir}/open-vm-tools-%{version}-21223074/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/LICENSE %{buildroot}/usr/share/package-licenses/open-vm-tools/72e0f7bb7a473ce0afa59f6083d9efa0d5d4f3bd || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/checkvm/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/hgfsclient/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/lib/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/lib/jsmn/LICENSE %{buildroot}/usr/share/package-licenses/open-vm-tools/7b20de0c23cbc9a17c3af51ddac5c3ad8182f8b1 || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/libDeployPkg/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/libappmonitor/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/libguestStoreClient/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/libguestlib/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/libhgfs/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/libvmtools/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/m4/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/modules/freebsd/vmblock/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/ef57706af82ae0d47d226c5c771aea1ef819c31e || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/modules/freebsd/vmmemctl/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/modules/solaris/vmblock/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/64035e974cbf6df866c5a1ead4401b8d18ebeabc || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/modules/solaris/vmhgfs/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/64035e974cbf6df866c5a1ead4401b8d18ebeabc || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/modules/solaris/vmmemctl/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/64035e974cbf6df866c5a1ead4401b8d18ebeabc || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/modules/solaris/vmxnet/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/64035e974cbf6df866c5a1ead4401b8d18ebeabc || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/modules/solaris/vmxnet3/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/64035e974cbf6df866c5a1ead4401b8d18ebeabc || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/namespacetool/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/rpctool/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/scripts/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/appInfo/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/componentMgr/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/containerInfo/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/deployPkg/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/desktopEvents/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/dndcp/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/gdp/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/guestInfo/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/guestStore/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/hgfsServer/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/powerOps/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/resolutionKMS/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/resolutionSet/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/serviceDiscovery/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/timeSync/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/vix/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/plugins/vmbackup/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/services/vmtoolsd/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/tests/testDebug/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/tests/testPlugin/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/tests/testVmblock/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/tests/vmrpcdbg/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/toolbox/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/vgauth/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/vgauthImport/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/vmblock-fuse/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/vmblockmounter/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/vmhgfs-fuse/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/vmware-user-suid-wrapper/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/vmwgfxctrl/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
cp %{_builddir}/open-vm-tools-%{version}-21223074/xferlogs/COPYING %{buildroot}/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/open-vm-tools.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/vmware-vmblock-fuse.service
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../open-vm-tools.service  %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../vmware-vmblock-fuse.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
mkdir -p %{buildroot}/usr/share/xdg/autostart
mv %{buildroot}/usr/share/defaults/open-vm-tools/xdg/autostart/vmware-user.desktop %{buildroot}/usr/share/xdg/autostart/
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/open-vm-tools.service
/usr/lib/systemd/system/multi-user.target.wants/vmware-vmblock-fuse.service

%files bin
%defattr(-,root,root,-)
/usr/bin/vm-support
/usr/bin/vmhgfs-fuse
/usr/bin/vmtoolsd
/usr/bin/vmware-checkvm
/usr/bin/vmware-hgfsclient
/usr/bin/vmware-namespace-cmd
/usr/bin/vmware-rpctool
/usr/bin/vmware-toolbox-cmd
/usr/bin/vmware-user
/usr/bin/vmware-vmblock-fuse
/usr/bin/vmware-xferlogs
/usr/bin/vmwgfxctrl

%files config
%defattr(-,root,root,-)
%attr(0644,root,root) /usr/lib/udev/rules.d/99-vmware-scsi-udev.rules

%files data
%defattr(-,root,root,-)
/usr/share/defaults/open-vm-tools/vmware-tools/poweroff-vm-default
/usr/share/defaults/open-vm-tools/vmware-tools/poweron-vm-default
/usr/share/defaults/open-vm-tools/vmware-tools/resume-vm-default
/usr/share/defaults/open-vm-tools/vmware-tools/scripts/vmware/network
/usr/share/defaults/open-vm-tools/vmware-tools/statechange.subr
/usr/share/defaults/open-vm-tools/vmware-tools/suspend-vm-default
/usr/share/defaults/open-vm-tools/vmware-tools/tools.conf.example
/usr/share/open-vm-tools/messages/de/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/de/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/en/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/en/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/es/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/es/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/fr/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/fr/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/it/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/it/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/ja/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/ja/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/ko/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/ko/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/zh_CN/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/zh_CN/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/zh_TW/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/zh_TW/vmtoolsd.vmsg
/usr/share/pam.d/vmtoolsd

%files dev
%defattr(-,root,root,-)
/usr/include/libDeployPkg/deployPkgFormat.h
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
/usr/lib64/libguestStoreClient.so
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
/usr/lib64/open-vm-tools/plugins/vmusr/libdndcp.so
/usr/lib64/open-vm-tools/plugins/vmusr/libresolutionSet.so
/usr/share/xdg/autostart/vmware-user.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/libDeployPkg.so.0
/usr/lib64/libDeployPkg.so.0.0.0
/usr/lib64/libguestStoreClient.so.0
/usr/lib64/libguestStoreClient.so.0.0.0
/usr/lib64/libguestlib.so.0
/usr/lib64/libguestlib.so.0.0.0
/usr/lib64/libhgfs.so.0
/usr/lib64/libhgfs.so.0.0.0
/usr/lib64/libvmtools.so.0
/usr/lib64/libvmtools.so.0.0.0
/usr/lib64/open-vm-tools/plugins/common/libhgfsServer.so
/usr/lib64/open-vm-tools/plugins/common/libvix.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libappInfo.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libcomponentMgr.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libdeployPkgPlugin.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libgdp.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libguestInfo.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libguestStore.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libpowerOps.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libresolutionKMS.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libtimeSync.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libvmbackup.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/open-vm-tools/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/open-vm-tools/64035e974cbf6df866c5a1ead4401b8d18ebeabc
/usr/share/package-licenses/open-vm-tools/70e5b527a568a6a75b977976e2d392fadf9bd84a
/usr/share/package-licenses/open-vm-tools/72e0f7bb7a473ce0afa59f6083d9efa0d5d4f3bd
/usr/share/package-licenses/open-vm-tools/7b20de0c23cbc9a17c3af51ddac5c3ad8182f8b1
/usr/share/package-licenses/open-vm-tools/ef57706af82ae0d47d226c5c771aea1ef819c31e

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/open-vm-tools.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/vmware-vmblock-fuse.service
/usr/lib/systemd/system/open-vm-tools.service
/usr/lib/systemd/system/vmware-vmblock-fuse.service

%files setuid
%defattr(-,root,root,-)
%attr(4755,root,root) /usr/bin/vmware-user-suid-wrapper
