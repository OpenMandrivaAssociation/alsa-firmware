%define version 1.0.27

%define firm_beta 0

%if %firm_beta
%define firm_name alsa-firmware-%version%firm_beta
%else
%define firm_name alsa-firmware-%version
%endif

Name:		alsa-firmware
Version:	%version
%if %firm_beta
Release:	0.%{firm_beta}.1
%else
Release:	1
%endif
Summary:	Advanced Linux Sound Architecture (ALSA) tools
# use the licenses figured out by Fedora, for a break down of where each license
# comes from see:
# http://pkgs.fedoraproject.org/gitweb/?p=alsa-firmware.git;a=blob;f=alsa-firmware.spec
License:	GPLv1+ and BSD and GPLv2+ and GPLv2 and LGPLv2+
URL:		http://alsa-project.org
Source0:	ftp://ftp.alsa-project.org/pub/firmware/%firm_name.tar.bz2
Source1:	audio_dock_netlist.h
Group:		System/Kernel and hardware
Requires:	alsa-tools-firmware >= %{version}
Requires:	udev
BuildRequires:	automake
BuildRequires:	autoconf
BuildArch:	noarch
Provides:	aica-firmware = %{version}-%{release}
Provides:	asihpi-firmware = %{version}-%{release}
Provides:	emu1010-firmware = %{version}-%{release}
Provides:	sb16-firmware = %{version}-%{release}
Provides:	korg1212-firmware = %{version}-%{release}
Provides:	maestro3-firmware = %{version}-%{release}
Provides:	turtlebeach-firmware = %{version}-%{release}
Provides:	yamaha-firmware = %{version}-%{release}
Provides:	ctexfx-firmware = %{version}-%{release}
Provides:	ctspeq-firmware = %{version}-%{release}
Obsoletes:	aica-firmware < %{version}-%{release}
Obsoletes:	asihpi-firmware < %{version}-%{release}
Obsoletes:	emagic-firmware < %{version}-%{release}
Obsoletes:	emagic-firmware < %{version}-%{release}
Obsoletes:	emu1010-firmware < %{version}-%{release}
Obsoletes:	sb16-firmware < %{version}-%{release}
Obsoletes:	korg1212-firmware < %{version}-%{release}
Obsoletes:	maestro3-firmware < %{version}-%{release}
Obsoletes:	turtlebeach-firmware < %{version}-%{release}
Obsoletes:	yamaha-firmware < %{version}-%{release}

# (ahmad) provide echomixer-firmware, and not echomixer, so as not to obsolete
# echomixer here and in alsa-tools; urpmi can't soomthly handle a package
# obsoleted by two packages
Provides:	echomixer-firmware = %{version}-%{release}

%description
This package contains the firmware binaries for a number of sound cards.
Some (but not all of these) require firmware loaders which are included in
the alsa-tools-firmware package.

%prep
%setup -q
cp %SOURCE1 emu/audio_dock_netlist.h

%build
libtoolize -c -f
autoreconf
%configure2_5x --with-hotplug-dir=/lib/firmware --disable-loader
%make

# (Fedora) Rename README files from firmware subdirs that have them
for i in hdsploader mixartloader pcxhrloader usx2yloader vxloader
do
  mv ${i}/README README.${i}
done

%install
%makeinstall_std

%files
%doc COPYING README*
/lib/firmware/aica_firmware.bin
/lib/firmware/asihpi
/lib/firmware/ea/
/lib/firmware/emu/
/lib/firmware/digiface_*
/lib/firmware/multiface_*
/lib/firmware/rpm_firmware.bin
/lib/firmware/korg/k1212.dsp
/lib/firmware/pcxhr/
/lib/firmware/vx/
/lib/firmware/turtlebeach/
/lib/firmware/yamaha/
/lib/firmware/sb16/
/lib/firmware/mixart/
/lib/firmware/ess/
/lib/firmware/ctefx.bin
/lib/firmware/ctspeq.bin
%dir %{_datadir}/alsa/firmware
%{_datadir}/alsa/firmware/usx2yloader
