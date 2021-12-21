Name: coeurl
Version: 0.1.1
Release: 1%{?dist}

License: MIT
URL: https://nheko.im/nheko-reborn/%{name}
Summary: Simple async wrapper around CURL for C++
Source0: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libevent-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: spdlog-devel

%description
Simple library to do http requests asynchronously via CURL in C++.

Based on the CURL-libevent example.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson \
    -Dwerror=false \
    -Dtests=false \
    -Dexamples=false
%meson_build

%install
%meson_install

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/lib%{name}.so.0*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Dec 21 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.1-1
- Updated to version 0.1.1.

* Fri Nov 19 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-1
- Updated to version 0.1.0.

* Fri Aug 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20210813git22f5892
- Initial release.
