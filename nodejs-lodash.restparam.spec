%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name lodash.restparam

Summary:       The modern build of lodash’s _.restParam as a module
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       3.6.1
Release:       4%{?dist}
License:       MIT
URL:           https://github.com/lodash/lodash
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
The modern build of lodash’s _.restParam as a module.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE.txt
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.6.1-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.6.1-3
- Rebuilt with updated metapackage

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 3.6.1-2
- Enable scl macros

* Thu Dec 17 2015 Troy Dawson <tdawson@redhat.com> - 3.6.1-1
- Initial package
