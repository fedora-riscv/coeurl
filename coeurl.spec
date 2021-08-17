%global commit0 22f58922da16c3b94d293d98a07cb7caa7a019e8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20210813

Name: coeurl
Version: 0
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: MIT
URL: https://nheko.im/nheko-reborn/%{name}
Summary: Simple async wrapper around CURL for C++
Source0: %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

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
%autosetup -n %{name}-%{commit0} -p1

%build
%meson \
    -Dwerror=false \
    -Dtests=false \
    -Dexamples=false
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.0*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Aug 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20210813git22f5892
- Initial release.
