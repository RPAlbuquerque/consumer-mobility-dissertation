# Public Notebook Notes

The notebooks in this directory are public analytical copies prepared from the restricted working notebooks used for Chapter 3. The following changes were made for responsible release:

- cell outputs, execution counts, and environment-specific metadata were cleared;
- private absolute paths were replaced with project-relative locations under `data/private/`;
- personal computing-account names and file references that could identify the focal manufacturer were removed;
- inline package-installation commands were replaced by the dependency specifications in `../environment/requirements.txt`;
- superseded or exploratory cells that were not part of the analytical workflow reported in the dissertation were excluded; and
- the retained overlap and flexible-model analyses were described as descriptive diagnostics of support, heterogeneity, and functional form rather than as estimates of causal effects.

No empirical observations, raw messages, device histories, individual trajectories, transaction records, credentials, or personally identifiable information are embedded in these notebooks. Full execution requires authorized access to the restricted inputs described in `../data/README.md`.

Users with authorized access to those inputs should not commit executed notebook outputs. Selected validation cells may display restricted source fields locally, so all outputs and execution counts must be cleared before a public commit.

These adaptations preserve the analytical procedures and interpretation reported in Chapter 3 while making the code inspectable without implying that the restricted data are openly reproducible.
