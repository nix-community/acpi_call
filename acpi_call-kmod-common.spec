%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     acpi_call-kmod-common
Version:  100.{{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  acpi_call module common package
License:  GPLv3
URL:      https://github.com/cr7pt0gt4ph7/acpi_call

VCS:      {{{ git_dir_vcs }}}
Source:   {{{ git_dir_pack }}}

# A small lie
Provides: acpi_call-kernel-modules-dkms = %{version}
Requires: acpi_call-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
acpi_call kernel module common package

%prep
{{{ git_dir_setup_macro }}}

%files
%doc README.md
%license LICENSE

%changelog
{{{ git_dir_changelog }}}
