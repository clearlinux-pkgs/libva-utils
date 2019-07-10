#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libva-utils
Version  : 2.5.0
Release  : 14
URL      : https://github.com/intel/libva-utils/archive/2.5.0.tar.gz
Source0  : https://github.com/intel/libva-utils/archive/2.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: libva-utils-bin = %{version}-%{release}
Requires: libva-utils-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libva-wayland)
BuildRequires : pkgconfig(libva-x11)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xfixes)

%description
[![Stories in Ready](https://badge.waffle.io/intel/libva-utils.png?label=ready&title=Ready)](http://waffle.io/intel/libva-utils)
[![Build Status](https://travis-ci.org/intel/libva-utils.svg?branch=master)](https://travis-ci.org/intel/libva-utils)
[![Coverity Scan Build Status](https://scan.coverity.com/projects/11613/badge.svg)](https://scan.coverity.com/projects/intel-libva-utils)

%package bin
Summary: bin components for the libva-utils package.
Group: Binaries
Requires: libva-utils-license = %{version}-%{release}

%description bin
bin components for the libva-utils package.


%package license
Summary: license components for the libva-utils package.
Group: Default

%description license
license components for the libva-utils package.


%prep
%setup -q -n libva-utils-2.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1562801446
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1562801446
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libva-utils
cp COPYING %{buildroot}/usr/share/package-licenses/libva-utils/COPYING
cp test/gtest/LICENSE %{buildroot}/usr/share/package-licenses/libva-utils/test_gtest_LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/avcenc
/usr/bin/avcstreamoutdemo
/usr/bin/h264encode
/usr/bin/hevcencode
/usr/bin/jpegenc
/usr/bin/loadjpeg
/usr/bin/mpeg2vaenc
/usr/bin/mpeg2vldemo
/usr/bin/putsurface
/usr/bin/putsurface_wayland
/usr/bin/sfcsample
/usr/bin/vainfo
/usr/bin/vavpp
/usr/bin/vp8enc
/usr/bin/vp9enc
/usr/bin/vppblending
/usr/bin/vppchromasitting
/usr/bin/vppdenoise
/usr/bin/vppscaling_csc
/usr/bin/vppsharpness

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libva-utils/COPYING
/usr/share/package-licenses/libva-utils/test_gtest_LICENSE
