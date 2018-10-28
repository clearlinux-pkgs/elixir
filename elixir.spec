#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : elixir
Version  : 1.7.4
Release  : 3
URL      : https://github.com/elixir-lang/elixir/archive/v1.7.4.tar.gz
Source0  : https://github.com/elixir-lang/elixir/archive/v1.7.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: elixir-bin = %{version}-%{release}
Requires: elixir-license = %{version}-%{release}
Requires: elixir-man = %{version}-%{release}
BuildRequires : otp
BuildRequires : otp-bin
BuildRequires : otp-dev
Patch1: build.patch

%description
![Elixir](https://github.com/elixir-lang/elixir-lang.github.com/raw/master/images/logo/logo.png)
=========
[![Travis build](https://secure.travis-ci.org/elixir-lang/elixir.svg?branch=master
"Build Status")](https://travis-ci.org/elixir-lang/elixir)

%package bin
Summary: bin components for the elixir package.
Group: Binaries
Requires: elixir-license = %{version}-%{release}
Requires: elixir-man = %{version}-%{release}

%description bin
bin components for the elixir package.


%package license
Summary: license components for the elixir package.
Group: Default

%description license
license components for the elixir package.


%package man
Summary: man components for the elixir package.
Group: Default

%description man
man components for the elixir package.


%prep
%setup -q -n elixir-1.7.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540765111
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1540765111
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/elixir
cp LICENSE %{buildroot}/usr/share/package-licenses/elixir/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/elixir/NOTICE
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/elixir/bin/elixir
/usr/lib/elixir/bin/elixirc
/usr/lib/elixir/bin/iex
/usr/lib/elixir/bin/mix
/usr/lib/elixir/lib/eex/ebin/Elixir.EEx.Compiler.beam
/usr/lib/elixir/lib/eex/ebin/Elixir.EEx.Engine.beam
/usr/lib/elixir/lib/eex/ebin/Elixir.EEx.SmartEngine.beam
/usr/lib/elixir/lib/eex/ebin/Elixir.EEx.SyntaxError.beam
/usr/lib/elixir/lib/eex/ebin/Elixir.EEx.Tokenizer.beam
/usr/lib/elixir/lib/eex/ebin/Elixir.EEx.beam
/usr/lib/elixir/lib/eex/ebin/eex.app
/usr/lib/elixir/lib/elixir/ebin/Elixir.Access.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Agent.Server.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Agent.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Application.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.ArgumentError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.ArithmeticError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Atom.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.BadArityError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.BadBooleanError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.BadFunctionError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.BadMapError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.BadStructError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Base.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Behaviour.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Bitwise.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Calendar.ISO.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Calendar.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.CaseClauseError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Code.Formatter.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Code.Identifier.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Code.LoadError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Code.Typespec.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Code.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Collectable.BitString.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Collectable.File.Stream.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Collectable.HashDict.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Collectable.HashSet.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Collectable.IO.Stream.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Collectable.List.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Collectable.Map.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Collectable.MapSet.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Collectable.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.CompileError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.CondClauseError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Date.Range.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Date.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.DateTime.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Dict.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.DynamicSupervisor.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enum.EmptyError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enum.OutOfBoundsError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enum.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.Date.Range.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.File.Stream.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.Function.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.GenEvent.Stream.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.HashDict.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.HashSet.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.IO.Stream.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.List.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.Map.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.MapSet.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.Range.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.Stream.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Enumerable.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.ErlangError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Exception.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.File.CopyError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.File.Error.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.File.LinkError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.File.Stat.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.File.Stream.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.File.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Float.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Function.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.FunctionClauseError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.GenEvent.Stream.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.GenEvent.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.GenServer.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.HashDict.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.HashSet.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.IO.ANSI.Docs.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.IO.ANSI.Sequence.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.IO.ANSI.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.IO.Stream.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.IO.StreamError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.IO.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Algebra.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Any.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Atom.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.BitString.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Date.Range.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Date.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.DateTime.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Error.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Float.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Function.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.HashDict.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.HashSet.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Integer.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.List.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Map.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.MapSet.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.NaiveDateTime.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Opts.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.PID.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Port.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Range.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Reference.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Regex.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Stream.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Time.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Tuple.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Version.Requirement.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.Version.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Inspect.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Integer.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Kernel.CLI.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Kernel.ErrorHandler.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Kernel.LexicalTracker.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Kernel.ParallelCompiler.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Kernel.ParallelRequire.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Kernel.SpecialForms.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Kernel.Typespec.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Kernel.Utils.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Kernel.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.KeyError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Keyword.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.List.Chars.Atom.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.List.Chars.BitString.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.List.Chars.Float.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.List.Chars.Integer.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.List.Chars.List.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.List.Chars.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.List.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Macro.Env.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Macro.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Map.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.MapSet.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.MatchError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Module.LocalsTracker.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Module.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.NaiveDateTime.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Node.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.OptionParser.ParseError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.OptionParser.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Path.Wildcard.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Path.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Port.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Process.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Protocol.UndefinedError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Protocol.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Range.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Record.Extractor.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Record.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Regex.CompileError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Regex.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Registry.Partition.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Registry.Supervisor.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Registry.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.RuntimeError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Set.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Stream.Reducers.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Stream.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Break.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Casing.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.Atom.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.BitString.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.Date.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.DateTime.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.Float.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.Integer.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.List.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.NaiveDateTime.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.Time.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.URI.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.Version.Requirement.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.Version.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Chars.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Normalizer.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Tokenizer.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.Unicode.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.String.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.StringIO.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Supervisor.Default.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Supervisor.Spec.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Supervisor.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.SyntaxError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.System.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.SystemLimitError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Task.Supervised.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Task.Supervisor.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Task.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Time.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.TokenMissingError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.TryClauseError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Tuple.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.URI.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.UndefinedFunctionError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.UnicodeConversionError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Version.InvalidRequirementError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Version.InvalidVersionError.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Version.Parser.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Version.Requirement.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.Version.beam
/usr/lib/elixir/lib/elixir/ebin/Elixir.WithClauseError.beam
/usr/lib/elixir/lib/elixir/ebin/elixir.app
/usr/lib/elixir/lib/elixir/ebin/elixir.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_aliases.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_bitstring.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_bootstrap.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_clauses.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_code_server.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_compiler.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_config.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_def.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_dispatch.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_env.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_erl.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_erl_clauses.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_erl_compiler.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_erl_for.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_erl_pass.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_erl_try.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_erl_var.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_errors.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_expand.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_fn.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_import.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_interpolation.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_lexical.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_locals.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_map.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_module.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_overridable.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_parser.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_quote.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_rewrite.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_sup.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_tokenizer.beam
/usr/lib/elixir/lib/elixir/ebin/elixir_utils.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.AssertionError.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.Assertions.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.CLIFormatter.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.Callbacks.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.CaptureIO.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.CaptureLog.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.CaptureServer.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.Case.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.CaseTemplate.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.Diff.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.DocTest.Error.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.DocTest.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.DuplicateDescribeError.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.DuplicateTestError.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.EventManager.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.FailuresManifest.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.Filters.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.Formatter.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.MultiError.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.OnExitHandler.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.Runner.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.RunnerStats.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.Server.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.Test.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.TestCase.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.TestModule.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.TimeoutError.beam
/usr/lib/elixir/lib/ex_unit/ebin/Elixir.ExUnit.beam
/usr/lib/elixir/lib/ex_unit/ebin/ex_unit.app
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.App.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Autocomplete.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.CLI.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Config.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Evaluator.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Helpers.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.History.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.Any.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.Atom.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.BitString.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.Date.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.Float.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.Function.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.Integer.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.List.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.Map.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.NaiveDateTime.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.PID.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.Port.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.Reference.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.Time.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.Tuple.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Info.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Introspection.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Pry.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Remsh.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.Server.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.State.beam
/usr/lib/elixir/lib/iex/ebin/Elixir.IEx.beam
/usr/lib/elixir/lib/iex/ebin/iex.app
/usr/lib/elixir/lib/logger/ebin/Elixir.Logger.App.beam
/usr/lib/elixir/lib/logger/ebin/Elixir.Logger.Backends.Console.beam
/usr/lib/elixir/lib/logger/ebin/Elixir.Logger.Config.beam
/usr/lib/elixir/lib/logger/ebin/Elixir.Logger.ErlangHandler.beam
/usr/lib/elixir/lib/logger/ebin/Elixir.Logger.ErrorHandler.beam
/usr/lib/elixir/lib/logger/ebin/Elixir.Logger.Formatter.beam
/usr/lib/elixir/lib/logger/ebin/Elixir.Logger.Translator.beam
/usr/lib/elixir/lib/logger/ebin/Elixir.Logger.Utils.beam
/usr/lib/elixir/lib/logger/ebin/Elixir.Logger.Watcher.beam
/usr/lib/elixir/lib/logger/ebin/Elixir.Logger.WatcherSupervisor.beam
/usr/lib/elixir/lib/logger/ebin/Elixir.Logger.beam
/usr/lib/elixir/lib/logger/ebin/logger.app
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.CLI.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Compilers.Elixir.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Compilers.Erlang.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Compilers.Test.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Config.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Dep.Converger.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Dep.ElixirSCM.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Dep.Fetcher.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Dep.Loader.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Dep.Lock.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Dep.Umbrella.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Dep.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.ElixirVersionError.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Error.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Generator.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Hex.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.InvalidTaskError.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Local.Installer.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Local.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.NoProjectError.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.NoTaskError.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Project.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.ProjectStack.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.PublicKey.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Rebar.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.RemoteConverger.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.SCM.Git.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.SCM.Path.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.SCM.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Shell.IO.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Shell.Process.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Shell.Quiet.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Shell.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.State.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Task.Compiler.Diagnostic.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Task.Compiler.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Task.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.App.Start.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.App.Tree.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Archive.Build.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Archive.Check.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Archive.Install.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Archive.Uninstall.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Archive.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Clean.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Cmd.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Compile.All.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Compile.App.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Compile.Elixir.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Compile.Erlang.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Compile.Leex.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Compile.Protocols.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Compile.Xref.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Compile.Yecc.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Compile.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Deps.Clean.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Deps.Compile.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Deps.Get.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Deps.Loadpaths.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Deps.Precompile.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Deps.Tree.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Deps.Unlock.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Deps.Update.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Deps.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Do.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Escript.Build.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Escript.Install.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Escript.Uninstall.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Escript.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Format.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Help.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Iex.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Loadconfig.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Loadpaths.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Local.Hex.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Local.PublicKeys.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Local.Rebar.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Local.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.New.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Profile.Cprof.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Profile.Eprof.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Profile.Fprof.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Run.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Test.Cover.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Test.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Tasks.Xref.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.TasksServer.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.Utils.beam
/usr/lib/elixir/lib/mix/ebin/Elixir.Mix.beam
/usr/lib/elixir/lib/mix/ebin/mix.app

%files bin
%defattr(-,root,root,-)
/usr/bin/elixir
/usr/bin/elixirc
/usr/bin/iex
/usr/bin/mix

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/elixir/LICENSE
/usr/share/package-licenses/elixir/NOTICE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/elixir.1
/usr/share/man/man1/elixirc.1
/usr/share/man/man1/iex.1
/usr/share/man/man1/mix.1
