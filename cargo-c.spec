%define _empty_manifest_terminate_build 0

Name:           cargo-c
Version:        0.9.16
Release:        1
Summary:        cargo applet to build and install C-ABI compatibile libraries
License:        BSD
# Also https://github.com/lu-zero/cargo-c
URL:            https://crates.io/crates/cargo-c
Source0:        https://github.com/lu-zero/cargo-c/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  rust
BuildRequires:  rust-src
BuildRequires:  cargo
BuildRequires:	pkgconfig(openssl)

%description
cargo applet to build and install C-ABI compatibile dynamic and static
libraries.

It produces and installs a correct pkg-config file, a static library
and a dynamic library, and a C header to be used by any C
(and C-compatible) software.

%prep
%autosetup -p1

%build
cargo build --release

%install
cargo install --root %{buildroot}%{_prefix} --no-track --path .

%files
%doc README.md
%license LICENSE
%{_bindir}/cargo-cbuild
%{_bindir}/cargo-cinstall
%{_bindir}/cargo-capi
%{_bindir}/cargo-ctest
