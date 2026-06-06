%global real_name pyogg

Name:           python-%{real_name}
Version:        0.6.14a1
Release:        2%{?dist}
Summary:        Simple OGG Vorbis, Opus and FLAC bindings for Python
License:        Unlicense
BuildArch:      noarch
URL:            https://github.com/TeamPyOgg/%{real_name}/

Source0:        %{url}/archive/%{version}.tar.gz#/%{real_name}-%{version}.tar.gz
Patch0:         %{name}-version.patch

BuildRequires:  python3-devel

%global _description %{expand:
PyOgg provides Python bindings for Xiph.org’s Opus, Vorbis and FLAC audio file
formats as well as their Ogg container format.}

%description %_description

%package -n     python3-%{real_name}
Summary:        %{summary}

%description -n python3-%{real_name} %_description

%prep
%autosetup -n PyOgg-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{real_name}

%check
%py3_check_import %{real_name}

%files -n python3-%{real_name} -f %{pyproject_files}
%license COPYING
%doc README.md

%changelog
* Sat Jun 06 2026 Simone Caronni <negativo17@gmail.com> - 0.6.14a1-2
- Fix version.

* Sat Jun 06 2026 Simone Caronni <negativo17@gmail.com> - 0.6.14a1-1
- First build.
