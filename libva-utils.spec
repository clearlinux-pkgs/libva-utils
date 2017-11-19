#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libva-utils
Version  : 2.0.0
Release  : 4
URL      : https://github.com/01org/libva-utils/releases/download/2.0.0/libva-utils-2.0.0.tar.bz2
Source0  : https://github.com/01org/libva-utils/releases/download/2.0.0/libva-utils-2.0.0.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: libva-utils-bin
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
### Generic Build Instructions ###
#### Setup ####
To build Google Test and your tests that use it, you need to tell your
build system where to find its headers and source files.  The exact
way to do it depends on which build system you use, and is usually
straightforward.

%package bin
Summary: bin components for the libva-utils package.
Group: Binaries

%description bin
bin components for the libva-utils package.


%prep
%setup -q -n libva-utils-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511117334
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1511117334
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/avcenc
/usr/bin/h264encode
/usr/bin/jpegenc
/usr/bin/loadjpeg
/usr/bin/mpeg2vaenc
/usr/bin/mpeg2vldemo
/usr/bin/putsurface
/usr/bin/putsurface_wayland
/usr/bin/vainfo
/usr/bin/vavpp
/usr/bin/vp9enc
