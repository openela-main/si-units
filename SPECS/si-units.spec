Name:          si-units
Version:       0.6.5
Release:       2%{?dist}
Summary:       International System of Units (JSR 363)
License:       BSD
URL:           https://github.com/unitsofmeasurement/%{name}
Source0:       https://github.com/unitsofmeasurement/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: junit
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin
BuildRequires: maven-local
BuildRequires: maven-jar-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: mvn(javax.measure:unit-api)
BuildRequires: mvn(tec.uom:uom-parent:pom:)
BuildRequires: mvn(tec.uom:uom-se:pom:)

BuildArch:     noarch

%description
A library of SI quantities and unit types (JSR 363).

%package javadoc
Group: Documentation
BuildArch: noarch
Summary: Javadoc for the library of SI quantities and unit types

%description javadoc
This package contains documentation for the International System
of Units - a library of SI quantities and unit types (JSR 363).

%prep
%setup -q -n %{name}-%{version}

%pom_remove_plugin :maven-javadoc-plugin quantity
%pom_remove_plugin :maven-javadoc-plugin units-java8
%pom_disable_module units # use only Java 8+
%pom_xpath_remove "pom:properties/pom:si.quantity.version"
%pom_xpath_inject "pom:properties" "<si.quantity.version>%{version}</si.quantity.version>"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Tue Aug 08 2017 Lukas Berk <lberk@redhat.com> - 0.6.5-2
- Incorprate feedback from fedora review tool.

* Wed Apr 12 2017 Nathan Scott <nathans@redhat.com> - 0.6.5-1
- Update to latest upstream sources.

* Wed Mar 22 2017 Nathan Scott <nathans@redhat.com> - 0.6.3-2
- Incorprate feedback from gil cattaneo on all uom packages.

* Mon Mar 06 2017 Nathan Scott <nathans@redhat.com> - 0.6.3-1
- Update to latest upstream sources.

* Tue Feb 28 2017 Nathan Scott <nathans@redhat.com> - 0.6.2-2
- Resolve lintian errors - source, license, documentation.

* Fri Feb 24 2017 Nathan Scott <nathans@redhat.com> - 0.6.2-1
- Switch to enabling the Java 8+ maven modules only now.
- Add unitsofmeasurement prefix to package name.
- Update to latest upstream sources.

* Thu Oct 13 2016 Nathan Scott <nathans@redhat.com> - 0.6-1
- Initial version.
