Summary:	Advanced Linux Sound Architecture (ALSA) tools
Name:		alsa-firmware
Version:	1.0.29
Release:	2
# use the licenses figured out by Fedora, for a break down of where each license
# comes from see:
# http://pkgs.fedoraproject.org/gitweb/?p=alsa-firmware.git;a=blob;f=alsa-firmware.spec
Group:		System/Kernel and hardware
License:	GPLv1+ and BSD and GPLv2+ and GPLv2 and LGPLv2+
Url:		http://alsa-project.org
Source0:	ftp://ftp.alsa-project.org/pub/firmware/%{name}-%{version}.tar.bz2
Source1:	audio_dock_netlist.h
BuildArch:	noarch
Requires:	alsa-tools-firmware >= %{version}
Requires:	udev

%rename		aica-firmware
%rename		asihpi-firmware
%rename		emu1010-firmware
%rename		sb16-firmware
%rename		korg1212-firmware
%rename		maestro3-firmware
%rename		turtlebeach-firmware
%rename		yamaha-firmware
Provides:	ctexfx-firmware = %{version}-%{release}
Provides:	ctspeq-firmware = %{version}-%{release}
Obsoletes:	emagic-firmware < %{version}-%{release}
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
cp %{SOURCE1} emu/audio_dock_netlist.h

%build
%configure \
	--with-hotplug-dir=/lib/firmware \
	--disable-loader

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
/lib/firmware/cs46xx/ba1
/lib/firmware/cs46xx/cwc4630
/lib/firmware/cs46xx/cwcasync
/lib/firmware/cs46xx/cwcbinhack
/lib/firmware/cs46xx/cwcdma
/lib/firmware/cs46xx/cwcsnoop
%dir %{_datadir}/alsa/firmware
%{_datadir}/alsa/firmware/usx2yloader
