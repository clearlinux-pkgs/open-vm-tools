#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : open-vm-tools
Version  : 10.1.10.6082533
Release  : 4
URL      : https://github.com/vmware/open-vm-tools/releases/download/stable-10.1.10/open-vm-tools-10.1.10-6082533.tar.gz
Source0  : https://github.com/vmware/open-vm-tools/releases/download/stable-10.1.10/open-vm-tools-10.1.10-6082533.tar.gz
Source1  : open-vm-tools.service
Summary  : Library for unpacking and executing VMware Guest Customization package.
Group    : Development/Tools
License  : BSD-2-Clause CDDL-1.0 GPL-2.0 LGPL-2.1
Requires: open-vm-tools-bin
Requires: open-vm-tools-autostart
Requires: open-vm-tools-config
Requires: open-vm-tools-lib
Requires: open-vm-tools-doc
Requires: open-vm-tools-data
BuildRequires : Linux-PAM-dev
BuildRequires : doxygen
BuildRequires : glib-dev
BuildRequires : graphviz
BuildRequires : gtk3-dev
BuildRequires : libSM-dev
BuildRequires : libXext-dev
BuildRequires : libmspack-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xtst)
BuildRequires : procps-ng-dev
BuildRequires : sed
Patch1: build.patch

%description
Project information:
open-vm-tools <https://github.com/vmware/open-vm-tools>
These are the release notes for the open-vm-tools.  Read them carefully, as
they explain how to build this project for different platforms and various
different Linux distributions.

%package autostart
Summary: autostart components for the open-vm-tools package.
Group: Default

%description autostart
autostart components for the open-vm-tools package.


%package bin
Summary: bin components for the open-vm-tools package.
Group: Binaries
Requires: open-vm-tools-data
Requires: open-vm-tools-config

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
Requires: open-vm-tools-lib
Requires: open-vm-tools-bin
Requires: open-vm-tools-data
Provides: open-vm-tools-devel

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
Requires: open-vm-tools-data
Requires: open-vm-tools-config

%description lib
lib components for the open-vm-tools package.


%prep
%setup -q -n open-vm-tools-10.1.10-6082533
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506648201
%configure --disable-static --without-xerces-c \
--without-xerces \
--without-gtkmm \
--without-dnet \
--without-gtkmm3 \
--without-gtk2 \
--with-gtk3
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1506648201
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/open-vm-tools.service
## make_install_append content
rm %{buildroot}/sbin/mount.vmhgfs
mkdir -p %{buildroot}//usr/lib/systemd/system/multi-user.target.wants
ln -s ../open-vm-tools.service  %{buildroot}//usr/lib/systemd/system/multi-user.target.wants
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/open-vm-tools.service

%files bin
%defattr(-,root,root,-)
/usr/bin/mount.vmhgfs
/usr/bin/vmtoolsd
/usr/bin/vmware-checkvm
/usr/bin/vmware-guestproxycerttool
/usr/bin/vmware-hgfsclient
/usr/bin/vmware-namespace-cmd
/usr/bin/vmware-rpctool
/usr/bin/vmware-toolbox-cmd
/usr/bin/vmware-user-suid-wrapper
/usr/bin/vmware-xferlogs

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/open-vm-tools.service
/usr/lib/systemd/system/open-vm-tools.service
/usr/lib/udev/rules.d/99-vmware-scsi-udev.rules

%files data
%defattr(-,root,root,-)
/usr/share/open-vm-tools/messages/de/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/de/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/ja/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/ja/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/ko/toolboxcmd.vmsg
/usr/share/open-vm-tools/messages/ko/vmtoolsd.vmsg
/usr/share/open-vm-tools/messages/zh_CN/toolboxcmd.vmsg

%files dev
%defattr(-,root,root,-)
/usr/include/libDeployPkg/guestcust-events.h
/usr/include/libDeployPkg/imgcust-api.h
/usr/include/libDeployPkg/includeCheck.h
/usr/include/libDeployPkg/linuxDeployment.h
/usr/include/libDeployPkg/log.h
/usr/include/libDeployPkg/process.h
/usr/include/libDeployPkg/rpcout.h
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
%defattr(-,root,root,-)
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
/usr/lib64/open-vm-tools/plugins/vmsvc/libtimeSync.so
/usr/lib64/open-vm-tools/plugins/vmsvc/libvmbackup.so
